from connection import app,db1
from models import Headlines
import flask



@app.route('/')
def home():
    return 'Home'


@app.route('/add_one')
def add_one():
    db1.NDTVapi.insert_one({"title":"Hello", "desc":'hello1'})
    return flask.jsonify(message="Success")



