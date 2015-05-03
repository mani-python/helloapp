#!/usr/bin/env python
from flask import Flask,request,render_template,url_for,redirect,flash,make_response

""" make_response modifies the response """

app = Flask(__name__)


@app.route('/login' , methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if passwordcheck(
             request.form.get('username'),
             request.form.get('password')
         ):
            flash ("Successfully logged in")
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('username', request.form.get('username'))
            return response
        else:
            error = "Incorrect username or password"
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('username','', expires=0)
    return response


@app.route('/')
def welcome():
    username = request.cookies.get("username")
    if username:
        return render_template('welcome.html', username=username)
    else:
        return redirect(url_for('login'))


def passwordcheck(username, password):
    if username == password:
        return True
    else:
        return False
if __name__ == '__main__':
    app.secret_key = 'Supersecret'
    app.debug = True
    app.run()

