from app import db

class Postings(db.Model):
    __tablename__ = 'postings'
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    price = db.Column(db.String)
