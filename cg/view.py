from flask import Flask, Blueprint, request
from cg.scheduler import Scheduler

views = Blueprint('views', __name__) 

"""search with a set of criteria"""
@views.route('/', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        postal = request.values.get('postal')
        distance = request.values.get('distance')
        return 'arguments are "{}" "{}"'.format(postal, distance)

    else :
        return 'in else case of search()'

"""updates session details"""
@views.route('/update', methods=['PUT'])
def update():
    """used in 'save' button"""
    return 'update api in put'

"""get results of specified session"""
@views.route('/session')
def get_session():
    """makes database query for the units associated with the session"""
    session = request.args.get('sess')
    return 'the session is {}'.format(session)

""""gets all session"""
@views.route('/getall')
def get_all_session():
    """makes database query for all the sessions"""
    return 'get_all_session()'

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
def get_all_sess():
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
    Scheduler(create=True)
    return 'created database'

if __name__ == '__main__':
    pass