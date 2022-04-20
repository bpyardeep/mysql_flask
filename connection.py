"""
The whole point of connection.py is to make connections with databases and stuff. We'll see where it goes in the future.

"""




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mysqlCred import MysqlCreds
from flask_mongoengine import MongoEngine
from pymongo import MongoClient, mongo_client
from flask_pymongo import PyMongo



app = Flask(__name__)




"""
Commented because not using mysql as of now. 
"""

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/{}'.format(MysqlCreds.USERNAME, MysqlCreds.PASSWORD,MysqlCreds.DB_NAME)
#db = SQLAlchemy(app)




# mongodb_client = PyMongo(app, uri = "mongodb://localhost:27017/NDTVapi")
# db1 = mongodb_client.db



if __name__ == "__main__":
    app.run(debug=True)




