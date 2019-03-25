from app import db
import sqlalchemy
import pandas as pd


class Course(db.Model):
    __tablename__ = 'Courses'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String)
    classes = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'course': self.course,
            'classes': self.classes,
        }

    def __repr__(self):
        return "<Course(course='%s', classes='[%s]'>" % (self.course, self.classes)


class Professor(db.Model):
    __tablename__ = 'Professors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    courses = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'courses': self.courses,
        }

    def __repr__(self):
        return "<Professor(name='%s', courses='[%s]'>" % (self.name, self.courses)


class Room(db.Model):
    __tablename__ = 'Rooms'

    id = db.Column(db.Integer, primary_key=True)
    cc = db.Column(db.String)
    lec = db.Column(db.String)
    lab = db.Column(db.String)
    tt = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'cc': self.cc,
            'lec': self.lec,
            'lab': self.lab,
            'tt': self.tt,
        }

    def __repr__(self):
        return "<Room(cc='%s', lec='%s', lab='%s', tt='%s'>" % (self.cc, self.lec, self.lab, self.tt)


class StudentGroup(db.Model):
    __tablename__ = 'Student Groups'

    id = db.Column(db.Integer, primary_key=True)
    student_group = db.Column(db.String)
    courses = db.Column(db.String)

    @property 
    def serialize(self):
        return {
            'id': self.id,
            'student_group': self.student_group,
            'courses': self.courses
        }

    def __repr__(self):
        return "<StudentGroup(student group='%s', courses='[%s]'>" % (self.student_group, self.courses)


db.create_all()

df_professors = pd.read_csv("data/professors.csv", dtype=str)
df_courses = pd.read_csv("data/courses.csv", dtype=str)
df_rooms = pd.read_csv("data/rooms.csv", dtype=str)
df_student_groups = pd.read_csv("data/student_groups.csv", dtype=str)

for row in df_professors.iterrows():
    prof = Professor(name=row[1]['Name'], courses=row[1]['Courses'])
    db.session.add(prof)

for row in df_courses.iterrows():
    course = Course(course=row[1]['Course'], classes=row[1]['Class'])
    db.session.add(course)

for row in df_rooms.iterrows():
    room = Room(cc=row[1]['CC'], lec=row[1]['LEC'],
                lab=row[1]['LAB'], tt=row[1]['TT'])
    db.session.add(room)

for row in df_student_groups.iterrows():
    sg = StudentGroup(student_group=row[1]['Student Groups'],
                      courses=row[1]['Courses'])
    db.session.add(sg)

db.session.commit()
