from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

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

@app.route('/show/<int:id>')
def profile(id):
    data = {
            'user_id': id
    }
    user = User.get_user_by_id(data)
    return render_template('showUser.html', user= user)


@app.route('/delete/<int:id>')
def deleteUser(id):
    data = {
        'user_id': id
    }
    user = User.get_user_by_id(data)
    # if session['user_id']==User['user_id']:
    User.destroyUser(data)
        # return redirect(request.referrer)
    return redirect(request.referrer)

@app.route('/showEditUser/<int:id>')
def ShowEditUser(id):
    data = {
            'user_id': id
    }
    user = User.get_user_by_id(data)
    return render_template('editUser.html', user= user)

@app.route('/edit/<int:id>', methods=['POST'])
def edit_user(id):
    data = {
        'user_id': id,
        'firstname':request.form['firstname'],
        'lastname':request.form['lastname'],
        'email':request.form['email']
    }
    User.editUser(data)
    return redirect('/users')


@app.route('/logout')
def Logout():
    session.clear=()
    return redirect('/users/new')