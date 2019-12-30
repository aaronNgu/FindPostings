"""fills database"""
from cg.models import Unit, Session
from cg.scraper import Scraper
from cg.database import Database, db 
from flask_restful import Resource, fields, marshal_with

unit = {
    'title': fields.String,
    'price': fields.String,
    'link': fields.String, 
    'pid':fields.String,
}
session = {
    'postal' : fields.String,
    'distance_from' : fields.Integer,
}

class Scheduler(Resource):
    
    def __init__(self, create=False):
        self.dtb = Database(db, create_db=create)

    def create_database(self):
        Database(db, create_db=True)

    def add_unit_to_database(self, ptl,  distance, session):
        sc = Scraper()
        sc.get_all_postings_for_item('apa', search_distance=distance, postal=ptl)
        postings = sc.get_postings()

        for post in postings:
            unit = Unit(title=post['title'], price=post['price'],\
            link=post['link'], pid=post['pid'], bedroom=post['bedroom'],\
            squarefoot=post['squareFoot'], sess_id=session.sess_id)
            self.dtb.add_single_item(unit)

    def add_session_to_database(self, post, dts):
        sess = Session(postal=post,distance_from=dts)
        self.dtb.add_single_item(sess)
        return sess

    @marshal_with(unit, envelope='units')
    def get_all_Unit(self):
        return self.dtb.query_all_from_table(Unit)

    @marshal_with(session, envelope='session')
    def get_all_Session(self):
        return self.dtb.query_all_from_table(Session)

    def delete_Unit_table(self):
        self.dtb.delete_all_rows_from_table(Unit)
    
    def delete_Session_table(self):
        self.dtb.delete_all_rows_from_table(Session)

    
if __name__ == '__main__':
    pass
