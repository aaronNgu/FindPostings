from flask import Flask, Blueprint
from cg.scheduler import Scheduler

views = Blueprint('views', __name__) 

@views.route('/')
def hello():
    return 'Hello` World'

@views.route('/<name>')
def hello_name(name):
    return 'Hello {}'.format(name)

@views.route('/addUnit')
def add_Unit():
    sch = Scheduler()
    sch.add_unit_to_database()
    return 'added unit to database'

@views.route('/addSession')
def add_session():
    sch = Scheduler()
    sch.add_session_to_database()
    return 'added session to database'

@views.route('/add/<postal>/<distance>')
def add(postal, distance):
    sch = Scheduler()
    session = sch.add_session_to_database(postal, distance)
    sch.add_unit_to_database(postal, distance, session)
    return 'added {} {}'.format(postal, distance)

@views.route('/getAllUnit')
def get_all_unit():
    sch = Scheduler()
    return sch.get_all_Unit()

@views.route('/getAllSession')
def get_all_session():
    sch = Scheduler()
    return sch.get_all_Session()

@views.route('/delete_unit')
def delete():
    sch = Scheduler()
    sch.delete_Unit_table()
    return 'deleted all unit'

@views.route('/delete_session')
def delete_session():
    sch = Scheduler()
    sch.delete_Session_table()
    return 'deleted all session'

@views.route('/createdb')
def create_database():
    sch = Scheduler()
    sch.create_database()
    return 'created database'

if __name__ == '__main__':
    pass