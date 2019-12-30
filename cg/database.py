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
        except:
            self.db.rollback()
            print("can't add item")
            pass

    def delete_all_rows_from_table(self, model):
        self.db.query(model).delete()
        self.db.commit()

    def query_all_from_table(self, model):
        """takes in a specified model from models.py"""
        return self.db.query(model).all()
   
    def get_db(self):
        return self.db        
