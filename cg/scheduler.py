"""fills database"""
from cg.models import Unit, Session
from cg.scraper import Scraper
from cg.database import Database, db 
from flask_restful import Resource, fields, marshal_with
import json

unit = {
    'title': fields.String,
    'price': fields.String,
}
session = {
    'postal' : fields.String,
    'distance_from' : fields.Integer,
}

class Scheduler(Resource):
    def create_database(self):
        Database(db, create_db=True)

    def add_unit_to_database(self):
        sc = Scraper()
        sc.get_all_postings_for_item('apa', search_distance='10', postal='V6T1Z4')
        postings = sc.get_postings()

        dtb = Database(db)
        for post in postings:
            post = Unit(title=post['title'], price=post['price'])
            dtb.add_single_item(post)

    def add_session_to_database(self):
        dtb = Database(db)
        dtb.add_single_item(Session(postal='V6T1Z4',distance_from=10))

    @marshal_with(unit, envelope='units')
    def get_all_Unit(self):
        dtb = Database(db)
        return dtb.query_all_from_table(Unit)

    @marshal_with(session, envelope='session')
    def get_all_Session(self):
        dtb = Database(db)
        return dtb.query_all_from_table(Session)

    def delete_Unit_table(self):
        dtb = Database(db)
        dtb.delete_all_rows_from_table(Unit)
    
    def delete_Session_table(self):
        dtb = Database(db)
        dtb.delete_all_rows_from_table(Session)

    
if __name__ == '__main__':
    pass
