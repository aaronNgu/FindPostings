from flask import Flask, Blueprint

view = Blueprint('view', __name__) 
@view.route('/')
def hello():
    return 'Hello World'

@view.route('/<name>')
def hello_name(name):
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    pass