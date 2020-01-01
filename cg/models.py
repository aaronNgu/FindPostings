"""Defined model of the database"""
from cg.database import db


class Session(db.Model):
    __tablename__ = 'session'
    sess_id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Date)
    keep = db.Column(db.Boolean)
    search_type = db.Column(db.String)
    postal = db.Column(db.String)
    distance_from = db.Column(db.Integer) 
    mx_price = db.Column(db.Integer)
    min_price = db.Column(db.Integer)
    min_bdr = db.Column(db.Integer)
    max_bdr = db.Column(db.Integer)

    email = db.Column(db.String)

    children = db.relationship('Unit', backref='session')

    def __repr__(self):
        return 'Session : postal = {} distance_from = {} time = {} keep {}'.format(self.postal, self.distance_from, self.time, self.keep)

class Unit(db.Model):

    __tablename__ = 'unit'
    apa_id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.String, unique=True)
    title = db.Column(db.String)
    price = db.Column(db.Integer)
    link = db.Column(db.String)
    bedroom = db.Column(db.String)
    squarefoot = db.Column(db.String)
    sess_id = db.Column(db.Integer, db.ForeignKey('session.sess_id'))

     
    def __repr__(self):
        return 'Unit : title = {} price = {}'.format(self.title, self.price)
