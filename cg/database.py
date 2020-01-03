"""wrapper class to interact with the database"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Database():
    #should have everything that represents the database

    def __init__(self, db, create_db=False):
        self.db = db.session
        if create_db: 
            db.create_all()

    def add_single_item(self, instance):
        #takes an SQLAlchemy object
        try: 
            self.db.add(instance)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("can't add item {}".format(e))
            pass

    def delete_all_rows_from_table(self, model):
        self.db.query(model).delete()
        self.db.commit()

    def delete_session(self, session, unit,  name):
        sess_id = self.db.query(session).filter_by(name=name).first().sess_id
        self.db.query(unit).filter_by(sess_id=sess_id).delete()
        self.db.query(session).filter_by(name=name).delete()
        self.db.commit()

    def query_all_from_table(self, model):
        """takes in a specified model from models.py"""
        return self.db.query(model).all()
   
    def query_session(self, model, session_name):
        return self.db.query(model).filter_by(name=session_name).first()

    def query_units_of_session(self, model, join_model, session_name):
        number = self.db.query(model).filter_by(name=session_name).first().sess_id
        return self.db.query(join_model).filter_by(sess_id=number).all()

    def get_db(self):
        return self.db        
