from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect ('/states')

@app.route('/states')
def state():
    dojos = Dojo.get_all()
    return render_template('index.html', all_dojos = dojos)

@app.route('/create/state', methods=['POST'])
def create():
    Dojo.create(request.form)
    return redirect('/states')
