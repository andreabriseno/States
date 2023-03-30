from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/cities')
def cities():

    return render_template('ninja.html', dojos= dojo.Dojo.get_all())

@app.route('/create/cities', methods=['POST'])
def createcity():
    ninja.Ninja.create(request.form)
    return redirect('/')