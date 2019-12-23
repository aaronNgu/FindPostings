from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
db= SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/<name>')
def hello_name(name):
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    app.run()