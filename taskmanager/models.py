# define database

from taskmanager import db

# will use the declarative base from SQLAlchemy 's model
class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)   
    # to reference the one-to-many-relationship - link to Task
    # backref establishes bidirectional relationship
    # lazy=True, which means that when we query the database for categories, 
    # it can simultaneously identify any task linked to the categories.
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True) 

    def __repr__(self):
        # __repr__ to represent itself in the form of a string 
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)                # db.Text allows for longer text inputs simplar to textarea 
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)   # if needed to include time also, use db.DateTime or db.Time
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string 
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
    

# To create database:
# Terminal:
# set_pg
# psql
# CREATE DATABASE MyDb;
# \c MyDB;
    
# python3 
# from taskmanager import app, db
# with app.app_context():
#   db.create_all()