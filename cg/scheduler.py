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
    'bedroom':fields.String,
    'date': fields.String,
    'squarefoot':fields.String,
    'time':fields.String
}
session = {
    'name':fields.String,
    'postal' : fields.String,
    'distance_from' : fields.Integer,
}

class Scheduler(Resource):
    
    def __init__(self, create=False):
        self.dtb = Database(db, create_db=create)
        self.sc = Scraper()

    def search(self, search_type, postal=None, distance=None, \
        mx_price=None, min_price=None, min_bdr=None, max_bdr=None):
        search_type = 'hhh' if not search_type else search_type
        self.sc.get_all_postings_for_item(search_type, \
            search_distance=distance, postal=postal, \
                min_price=min_price, max_price=mx_price, \
                    min_bedrooms=min_bdr, max_bedrooms=max_bdr)
        return self.sc.get_postings()

    def add_unit_to_database(self, ptl,  distance, session):
        sc = Scraper()
        sc.get_all_postings_for_item('apa', search_distance=distance, postal=ptl)
        postings = sc.get_postings()

        for post in postings:
            unit = Unit(title=post['title'], price=post['price'],\
            link=post['link'], pid=int(post['pid']), bedroom=post['bedroom'],\
            squarefoot=post['squareFoot'], sess_id=session.sess_id)
            self.dtb.add_single_item(unit)

    def add_session_to_database(self, search_type, name=None, postal=None, \
        distance=None, mx_price=None, min_price=None, min_bdr=None, max_bdr=None, email=None):
        sess = Session(name=name, search_type=search_type, postal=postal, distance_from=distance, \
            mx_price=mx_price, min_price=min_price, min_bdr=min_bdr, max_bdr=max_bdr, \
                 email=email)
        self.dtb.add_single_item(sess)
        return sess
    
    @marshal_with(session, envelope='session')
    def get_session(self, name):
        return self.dtb.query_session(Session, session_name=name)

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
