from flask import Flask, jsonify, request, json

from app import db, app
from models import Course, Professor, Room, StudentGroup

courses = Course.query.all()
professors = Professor.query.all()
rooms = Room.query.all()
sg = StudentGroup.query.all()

for c in courses:
    print(c.serialize)

for p in professors:
    print(p.serialize)

for r in rooms:
    print(r.serialize)

for s in sg:
    print(s.serialize)

print(len(courses))