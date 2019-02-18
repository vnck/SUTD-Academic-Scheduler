#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:09:46 2019

@author: joseph
"""

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import sqlalchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
bcrypt = Bcrypt(app)
Base = SQLAlchemy(app)

class Account(Base.Model):
    
    __tablename__ = 'Accounts'
    
    id = Base.Column(Base.Integer,primary_key=True)
    name = Base.Column(Base.String)
    initials = Base.Column(Base.String)
    hash_pass = Base.Column(sqlalchemy.types.LargeBinary)

    def __repr__(self):
        return "<Account(name='%s', initials='%s', hash_pass='%s')>" % ( self.name, self.initials, self.hash_pass)

Base.drop_all()
Base.create_all()
Base.session.add(Account(name="John", initials="J", hash_pass=bcrypt.generate_password_hash('hunter2')))
Base.session.commit()




# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        acc = Account.query.filter_by(name=request.form['username']).first()
        if acc==None:
            error = 'Invalid Credentials. Please try again.'
        elif bcrypt.check_password_hash(acc.hash_pass, request.form['password'])==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('welcome.html', error=error)  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

# Route for handling the login page logic


