#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 23:09:46 2019
@author: joseph
"""

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_bcrypt import Bcrypt
# import sqlalchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# bcrypt = Bcrypt(app)
# Base = SQLAlchemy(app)

# class Account(Base.Model):

#     __tablename__ = 'Accounts'

#     id = Base.Column(Base.Integer,primary_key=True)
#     name = Base.Column(Base.String, unique=True)
#     initials = Base.Column(Base.String)
#     hash_pass = Base.Column(sqlalchemy.types.LargeBinary)

#     def __repr__(self):
#         return "<Account(name='%s', initials='%s', hash_pass='%s')>" % ( self.name, self.initials, self.hash_pass)

# Base.drop_all()
# Base.create_all()
# Base.session.add(Account(name="John", initials="J", hash_pass=bcrypt.generate_password_hash('hunter2')))
# Base.session.commit()


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        user = data['user']
        password = data['password']
        print(user)
        print(password)
        if "user1" == user and "password" == password:
            response = jsonify(isAuthenticated=True, isCoordinator=True)
        elif "user2" == user and "password" == password:
            response = jsonify(isAuthenticated=True, isCoordinator=False)
        else:
            return jsonify(message='invalid authentication'), 500
    return response


# start the server with the 'run()' method
if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)

# Route for handling the login page logic
