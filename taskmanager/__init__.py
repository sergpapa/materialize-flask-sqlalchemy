# initialise taskmanager as a package
# allowing us to use our own imports, as well as any standard imports.

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env


app = Flask(__name__)                   #  create instance of Flask class stored in app variable. Default name =  __name__
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)                    #  instance of SQLAlchemy class - set to the instance of app Flask task

from taskmanager import routes          # importing routes from our own taskmanager package (we need app and db to run, this is why we do not import on top)