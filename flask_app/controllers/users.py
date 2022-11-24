from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    if user not in session:
        return redirect('/logout')
    return render_template('users.html')

@app.route('/users')
def showUsers():
    all_users=User.get_all()
    return render_template('users.html', users=all_users)

@app.route('/users/new')
def userNew():
    return render_template("createuser.html")

@app.route('/create/user', methods=['POST'])
def AddUser():
    data={
        'firstname':request.form['firstname'],
        'lastname':request.form['lastname'],
        'email':request.form['email']
    }
    User.Create_user(data)
    return redirect('/users')

@app.route('/logout')
def Logout():
    session.clear=()
    return redirect('/users/new')