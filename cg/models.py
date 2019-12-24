"""Defined model of the database"""
from cg.database import db

class Post(db.Model):

    __tablename__ = 'postings'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.String)
     
    def __repr__(self):
        return 'Post title: {} price: {}'.format(self.title, self.price)
