from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
#from flask_bcrypt import Bcrypt
import sqlalchemy
from app import app, db, bcrypt, UPLOAD_FOLDER
from models import Account, Request, CourseClass, Course, Professor
import Scheduler
import os


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        if Account.query.filter_by(user=data['user']).first() != None and bcrypt.check_password_hash(Account.query.filter_by(user=data['user']).first().password, data['password']):
            if Account.query.filter_by(user=data['user']).first().role == 'Coordinator':
                response = jsonify(name=Account.query.filter_by(user=data['user']).first().name,
                                   isAuthenticated=True,
                                   isCoordinator=True), 200
            else:
                response = jsonify(name=Account.query.filter_by(user=data['user']).first().name, isAuthenticated=True,
                                   isCoordinator=False), 200
        else:
            return jsonify(message='invalid authentication'), 500
    return response


@app.route('/get-schedule', methods=['GET'])
def get_schedule():
    course_classes = CourseClass.query.all()
    sched = []
    for cc in course_classes:
        cc_dict = {
            "course": cc.course,
            "studentGroups": cc.studentGroups,
            "professors": cc.professors,
            "day": cc.day,
            "startTime": cc.startTime,
            "endTime": cc.endTime,
            "room": cc.room
        }
        sched.append(cc_dict)
    return json.dumps(sched)


@app.route('/get-schedule-status', methods=['GET'])
def scheduler_status():
    return jsonify(message=Scheduler.running), 200


@app.route('/get-course-colors', methods=['GET'])
def get_course_colors():
    courses = Course.query.all()
    colorCodes = []
    for course in courses:
        cc = {
            "course": course.course,
            "color": course.colorCode
        }
        colorCodes.append(cc)
    return json.dumps(colorCodes)


@app.route('/generate-schedule', methods=['GET'])
def generate_schedule():
    if not Scheduler.running:
        try:
            Scheduler.running = True
            Scheduler.startAlgo()
            Scheduler.running = False
            response = jsonify(message='generating schedule'), 200
        except:
            response = jsonify(message='failed to generate'), 500
    else:
        response = jsonify(message='a scheduler is being generated'), 200
    return response


@app.route('/get-requests', methods=['GET'])
def get_request():
    req = Request.query.all()
    newls = []
    for i in range(len(req)):
        newls.append({})
        newls[i]["id"] = req[i].id
        newls[i]["day"] = req[i].day
        newls[i]["requester"] = req[i].requester
        newls[i]["startTime"] = req[i].startTime
        newls[i]["endTime"] = req[i].endTime
        newls[i]["reason"] = req[i].reason
        newls[i]["status"] = req[i].status
        newls[i]["weekly"] = req[i].weekly
    return json.dumps(newls)


@app.route('/get-satisfied', methods=['POST'])
def get_satisfied():
    satisfied = False
    if request.method == 'POST':
        data = request.get_json()
        if Professor.query.filter_by(name=data['name']).first() != None:
            satisfied = Professor.query.filter_by(
                name=data['name']).first().satisfied
            print(data['name'] + "  " + str(satisfied))
    return json.dumps(satisfied)


@app.route('/del-request', methods=['POST'])
def del_request():
    if request.method == 'POST':
        data = request.get_json()
        print(data['id'])
        db.session.delete(Request.query.filter_by(id=data['id']).first())
        db.session.commit()
        print(Request.query.all())
    req = Request.query.all()
    newls = []
    for i in range(len(req)):
        newls.append({})
        newls[i]["id"] = req[i].id
        newls[i]["day"] = req[i].day
        newls[i]["requester"] = req[i].requester
        newls[i]["startTime"] = req[i].startTime
        newls[i]["endTime"] = req[i].endTime
        newls[i]["reason"] = req[i].reason
        newls[i]["status"] = req[i].status
        newls[i]["weekly"] = req[i].weekly
    return json.dumps(newls)


@app.route('/approve-request', methods=['POST'])
def approve_request():
    if request.method == 'POST':
        data = request.get_json()
        status = Request.query.filter_by(id=data['id']).first()
        if (status.status == True):
            status.status = False
        elif (status.status == False):
            status.status = True
        db.session.commit()
    req = Request.query.all()
    newls = []
    for i in range(len(req)):
        newls.append({})
        newls[i]["id"] = req[i].id
        newls[i]["day"] = req[i].day
        newls[i]["requester"] = req[i].requester
        newls[i]["startTime"] = req[i].startTime
        newls[i]["endTime"] = req[i].endTime
        newls[i]["reason"] = req[i].reason
        newls[i]["status"] = req[i].status
        newls[i]["weekly"] = req[i].weekly
    return json.dumps(newls)


@app.route('/add-request', methods=['POST'])
def add_request():
    if request.method == 'POST':
        data = request.get_json()
        req1 = Request(day=data["daySelect"], requester=data["requester"], startTime=data["startTime"],
                       endTime=data["endTime"], reason=data["reason"], weekly=data["weekly"], status=False)
        db.session.add(req1)
        db.session.commit()
        print(Request.query.all())
    req = Request.query.all()
    newls = []
    for i in range(len(req)):
        newls.append({})
        newls[i]["id"] = req[i].id
        newls[i]["day"] = req[i].day
        newls[i]["requester"] = req[i].requester
        newls[i]["startTime"] = req[i].startTime
        newls[i]["endTime"] = req[i].endTime
        newls[i]["reason"] = req[i].reason
        newls[i]["status"] = req[i].status
        newls[i]["weekly"] = req[i].weekly
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


if __name__ == '__main__':
    CORS(app)
    app.run(debug=True)
