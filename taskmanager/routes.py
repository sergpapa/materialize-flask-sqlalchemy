# Here we are using our Flask routes to render the templates needed

from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task

@app.route("/")
def home():
    return render_template("base.html")