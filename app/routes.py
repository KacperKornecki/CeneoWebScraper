from unicodedata import name
from app import app
from flask import render_template

@app.route('/')

def index():
    name = 'Kacper Kornecki'
    return render_template("index.html.jinja", name=name)
