from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
#from flask_bcrypt import Bcrypt
import sqlalchemy
from app import app, db, bcrypt, UPLOAD_FOLDER
from models import Account, Request, CourseClass
import Scheduler
import os


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        if Account.query.filter_by(user=data['user']).first() != None and bcrypt.check_password_hash(Account.query.filter_by(user=data['user']).first().password, data['password']):
            if Account.query.filter_by(user=data['user']).first().role == 'Coordinator':
                response = jsonify(isAuthenticated=True,
                                   isCoordinator=True), 200
            else:
                response = jsonify(isAuthenticated=True,
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
    return json.dumps(newls)


@app.route('/del-requests', methods=['POST'])
def del_request():
    if request.method == 'POST':
        data = request.get_json()
        to_delete = Request.query.filter_by(id=data['id']).first()
        db.session.delete(to_delete)
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
    for i in range(len(req)):
        newls.append({})
        newls[i]["id"] = req[i].id
        newls[i]["day"] = req[i].day
        newls[i]["requester"] = req[i].requester
        newls[i]["startTime"] = req[i].startTime
        newls[i]["endTime"] = req[i].endTime
        newls[i]["reason"] = req[i].reason
        newls[i]["status"] = req[i].status
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
    app.run(debug=False)
