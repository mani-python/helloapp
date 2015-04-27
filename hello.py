#!/usr/bin/env python
from flask import Flask,request,render_template,url_for,redirect
app = Flask(__name__)


@app.route('/login' , methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if passwordcheck(
             request.form.get('username'),
             request.form.get('password')
         ):
            return redirect(url_for('welcome', username=request.form.get('username')))
        else:
            error = "Incorrect username or password"
    return render_template('login.html', error=error)


@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)


def passwordcheck(username, password):
    if username == password:
        return True
    else:
        return False
if __name__ == '__main__':
    app.debug = True
    app.run()

