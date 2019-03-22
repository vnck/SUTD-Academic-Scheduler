#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:21:43 2019

@author: joseph
"""

from flask import Flask, render_template, redirect, url_for, request,jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt
import sqlalchemy
from app import app,db,bcrypt
from models import Account,Professor,Course,CourseCoordinator,Room,StudentGroup,CourseClass



#Adding Courses
mycourse = Course(name="math")
mycourse2 = Course(name="science")

#Adding Professors/Course Coordinators
myprof = Professor(name="JJ",initials="j",hash_pass=bcrypt.generate_password_hash('hunter2'),courses=[mycourse])
myprof2 = Professor(name="GG",initials="G",hash_pass=bcrypt.generate_password_hash('gg'),courses=[mycourse,mycourse2])
mycourseco = CourseCoordinator(name="cc",initials="c",hash_pass=bcrypt.generate_password_hash('cc'))

#Adding rooms
myroom = Room(name="TT22",size=50,roomType="Think Tank")
myroom2 = Room(name="CC23",size=51,roomType="Cohort Class")

#Adding Student Groups
stg1= StudentGroup(name="cohort1",size="50")
stg2= StudentGroup(name="ISTD1",size="50")

#Adding CourseClass

cc1 = CourseClass(courses=[mycourse,mycourse2],
                    professorSize=2,
                    professors=[myprof,myprof2],
                    duration=3,
                    size=50,
                    classType="cohort class",
                    )

db.drop_all()
db.create_all()

#Adding Accounts/prof/coursecoordinators
db.session.add(myprof)
db.session.add(myprof2)
db.session.add(mycourseco)

#Adding Rooms
db.session.add(myroom)
db.session.add(myroom2)

#Adding Course StudentGroups
db.session.add(stg1)
db.session.add(stg2)

#adding course class
db.session.add(cc1)
db.session.commit()




# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/login', method='POST')
def login():
    if request.method == 'POST':
        data = request.data
        if Professor.query.filter_by(name=data.user).first().username!=None and bcrypt.check_password_hash(Professor.query.filter_by(name=data.user).first().hash_pass, data.password):
            response = jsonify(isAuthenticated= True, isCoordinator= False)
        elif CourseCoordinator.query.filter_by(name=data.user).first().username!=None and bcrypt.check_password_hash(CourseCoordinator.query.filter_by(name=data.user).first().hash_pass, data.password):
            response = jsonify(isAuthenticated= True, isCoordinator= True)
        else:
            return jsonify(message='invalid authentication'),500
    return response

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

# Route for handling the login page logic