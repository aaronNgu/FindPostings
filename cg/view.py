from flask import Flask, Blueprint, request, jsonify
from cg.scheduler import Scheduler

views = Blueprint('views', __name__) 

"""search with a set of criteria"""
@views.route('/', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        search_type = request.values.get('type')
        postal = request.values.get('postal')
        distance = request.values.get('distance')
        mx_price = request.values.get('mx_price')
        min_price = request.values.get('min_price')
        min_bdr = request.values.get('min_bdr')
        max_bdr = request.values.get('max_bdr')
        sch = Scheduler()
        return jsonify(sch.search(search_type, postal=postal,\
            distance=distance, mx_price=mx_price,\
                 min_price=min_price, min_bdr=min_bdr,\
                     max_bdr=max_bdr))
    else :
        return 'in else case of search()'

@views.route('/save', methods=['GET','POST'])
def save_session():
    if request.method == 'POST':
        name = request.values.get('name')
        search_type = request.values.get('type')
        postal = request.values.get('postal')
        distance = request.values.get('distance')
        mx_price = request.values.get('mx_price')
        min_price = request.values.get('min_price')
        min_bdr = request.values.get('min_bdr')
        max_bdr = request.values.get('max_bdr')
        email = request.values.get('email')
        sch = Scheduler()
        sch.add_session_to_database(search_type, name=name, postal=postal, \
            distance=distance, mx_price=mx_price, min_price=min_price, \
                min_bdr=min_bdr, max_bdr=max_bdr, email=email) 
        return 'saved session' 
    return "wasn't a post request"

"""updates session details"""
@views.route('/update', methods=['PUT'])
def update():
    """used in 'save' button"""
    return 'update api in put'

"""get results of specified session"""
@views.route('/session')
def get_results_of_session():
    return 'get results of session'

@views.route('/session')
def get_session():
    """makes database query for session with 'name'"""
    name = request.args.get('name')
    sch = Scheduler()
    return sch.get_session(name)

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