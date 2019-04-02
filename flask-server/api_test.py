#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 12:21:43 2019

@author: joseph
"""

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
#from flask_bcrypt import Bcrypt
import sqlalchemy
from app import app, db, bcrypt, UPLOAD_FOLDER
from models import Account, Professor, Course, CourseCoordinator, Room, StudentGroup, CourseClass, Request
import os


# Adding Courses
mycourse = Course(name="math")
mycourse2 = Course(name="science")

# Adding Professors/Course Coordinators
myprof = Professor(name="prof1", initials="j", hash_pass=bcrypt.generate_password_hash(
    '12345'), courses=[mycourse])
myprof2 = Professor(name="prof2", initials="G", hash_pass=bcrypt.generate_password_hash(
    '12345'), courses=[mycourse, mycourse2])
mycourseco = CourseCoordinator(
    name="coord1", initials="c", hash_pass=bcrypt.generate_password_hash('12345'))

# Adding rooms
myroom = Room(name="TT22", size=50, roomType="Think Tank")
myroom2 = Room(name="CC23", size=51, roomType="Cohort Class")

# Adding Student Groups
stg1 = StudentGroup(name="cohort1", size="50")
stg2 = StudentGroup(name="ISTD1", size="50")

# Adding CourseClass

cc1 = CourseClass(courses=[mycourse, mycourse2],
                  professorSize=2,
                  professors=[myprof, myprof2],
                  duration=3,
                  size=50,
                  classType="cohort class",
                  )

# Adding Request

req1 = Request(day="Thursday", requester="JJ", startTime="2pm",
               endTime="2pm", reason="lazy", status=False)
req2 = Request(day="Friday", requester="GG", startTime="2pm",
               endTime="2pm", reason="lazy", status=False)

db.drop_all()
db.create_all()

# Adding Accounts/prof/coursecoordinators
db.session.add(myprof)
db.session.add(myprof2)
db.session.add(mycourseco)

# Adding Rooms
db.session.add(myroom)
db.session.add(myroom2)

# Adding Course StudentGroups
db.session.add(stg1)
db.session.add(stg2)

# adding course class
db.session.add(cc1)

# adding request
db.session.add(req1)
db.session.add(req2)

# committing
db.session.commit()

# use decorators to link the function to a url


@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if Professor.query.filter_by(name=data['user']).first() != None and bcrypt.check_password_hash(Professor.query.filter_by(name=data['user']).first().hash_pass, data['password']):
            response = jsonify(isAuthenticated=True, isCoordinator=False)
        elif CourseCoordinator.query.filter_by(name=data['user']).first() != None and bcrypt.check_password_hash(CourseCoordinator.query.filter_by(name=data['user']).first().hash_pass, data['password']):
            response = jsonify(isAuthenticated=True, isCoordinator=True)
        else:
            return jsonify(message='invalid authentication'), 500
    return response


@app.route('/get-requests', methods=['GET'])
def get_request():
    req = Request.query.all()
    newls = []
    for i in range (len(req)):
        newls.append({})
        newls[i]["id"]=req[i].id
        newls[i]["day"]=req[i].day
        newls[i]["requester"]=req[i].requester
        newls[i]["startTime"]=req[i].startTime
        newls[i]["endTime"]=req[i].endTime
        newls[i]["reason"]=req[i].reason
        newls[i]["status"]=req[i].status
    return json.dumps(newls)


@app.route('/del-requests', methods=['POST'])
def del_request():
    if request.method == 'POST':
        data = request.get_json()
        to_delete = Request.query.filter_by(id=data['id']).first()
        db.session.delete(to_delete)
    req = Request.query.all()
    newls = []
    for i in range (len(req)):
        newls.append({})
        newls[i]["id"]=req[i].id
        newls[i]["day"]=req[i].day
        newls[i]["requester"]=req[i].requester
        newls[i]["startTime"]=req[i].startTime
        newls[i]["endTime"]=req[i].endTime
        newls[i]["reason"]=req[i].reason
        newls[i]["status"]=req[i].status
    return json.dumps(newls)

@app.route('/approve-requests', methods=['POST'])
def approve_request():
    if request.method == 'POST':
        data = request.get_json()
        status = Request.query.filter_by(id=data['id']).first()
        status.status = data['status']
        db.session.commit()
    req = Request.query.all()
    newls = []
    for i in range (len(req)):
        newls.append({})
        newls[i]["id"]=req[i].id
        newls[i]["day"]=req[i].day
        newls[i]["requester"]=req[i].requester
        newls[i]["startTime"]=req[i].startTime
        newls[i]["endTime"]=req[i].endTime
        newls[i]["reason"]=req[i].reason
        newls[i]["status"]=req[i].status
    return json.dumps(newls)

@app.route('/upload-inputs', methods=['POST'])
def fileUpload():
    target = UPLOAD_FOLDER
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = "input.csv"
    destination = "/".join([target, filename])
    try:
        file.save(destination)
        out = "OK"
    except:
        out = "NOT OK"
    return out


# start the server with the 'run()' method
if __name__ == '__main__':
    CORS(app)
    app.run(debug=False)

# Route for handling the login page logic
