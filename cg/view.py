from flask import Flask, Blueprint
from cg.scheduler import *

views = Blueprint('views', __name__) 

@views.route('/')
def hello():
    return 'Hello World'

@views.route('/<name>')
def hello_name(name):
    return 'Hello {}'.format(name)

@views.route('/getAll')
def get_all():
    return add_post_to_database()

if __name__ == '__main__':
    pass