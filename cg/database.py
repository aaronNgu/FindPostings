
class Database():
    #should have everything that represents the database

    def __init__(self, db):
        self.db = db.session

    def add_single_post(self, instance):
        #takes an Postings object
        self.db.add(instance)
        self.db.commit()

    def delete_all_rows_from_table(self, model):
        self.db.query(model).delete()
        self.db.commit()

    def query_all_from_table(self, model):
        """takes in a specified model from models.py"""
        return self.db.query(model).all()
   
    def get_db(self):
        return self.db        
