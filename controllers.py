from app import  app
from flask import render_template, url_for
from forms import Register
from models import  Registr

@app.route('/')
def home():
    return render_template('header.html')

@app.route('/reg')
def registration():
    registration = Registr.query.all()
    return render_template('registration.html', registration = registration)
