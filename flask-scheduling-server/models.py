from app import db, bcrypt
import sqlalchemy
import pandas as pd
import random


class Account(db.Model):
    __tablename__ = 'Accounts'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    role = db.Column(db.String)


class Course(db.Model):
    __tablename__ = 'Courses'

    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String)
    classes = db.Column(db.String)
    colorCode = db.Column(db.Integer)

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
    colorCode = db.Column(db.Integer)


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
    name = db.Column(db.String)
    req = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'req': self.req
        }

    def __repr__(self):
        return "<Room(name='%s', req='%s'>" % (self.name, self.req)


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


class HardBlocks(db.Model):
    __tablename__ = 'Hard Blocks'
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer)
    period = db.Column(db.Float)
    room = db.Column(db.String)
    reason = db.Column(db.String)

    def __repr__(self):
        return "<HardBlocks, day = {}, period ={}, room={}, reason={}>"\
            .format(self.day, self.period, self.room, self.reason)


class CourseClass(db.Model):
    __tablename__ = 'Course Class'

    id = db.Column(db.Integer, primary_key=True)
    studentGroups = db.Column(db.String)
    professors = db.Column(db.String)

    course = db.Column(db.String)
    room = db.Column(db.String)
    day = db.Column(db.Integer)
    startTime = db.Column(db.Float)
    endTime = db.Column(db.Float)

    def __repr__(self):
        return "<CourseclassDb,course = {} ,studentGroups = {},professors = {},day={},startTime={},endTime={},room = {}>"\
            .format(self.course, self.studentGroups, self.professors, self.day, self.startTime, self.endTime, self.room)


class Request(db.Model):
    __tablename__ = "Request"
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String, nullable=False)
    requester = db.Column(db.String, nullable=False)
    startTime = db.Column(db.String, nullable=False)
    endTime = db.Column(db.String, nullable=False)
    reason = db.Column(db.String, nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    weekly = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        # return {"id":self.id, "day": self.day, "requester": self.requester, "startTime": self.startTime, "endTime":self.endTime, "reason":self.reason,"status":self.status}
        return "<Request(id='%s',day='%s',requester='%s',startTime='%s',endTime='%s',reason='%s',status='%s',weekly='%s')>" % (str(self.id), self.day, self.requester, self.startTime, self.endTime, self.reason, self.status, self.weekly)


def createDB():
    """
    Warning do not call this in the middle of the application or all current data will be lost
    Removes the current DB and creates a new one from CSV
    """
    db.drop_all()
    db.create_all()

    df_professors = pd.read_csv("data/professors.csv", dtype=str)
    df_courses = pd.read_csv("data/courses.csv", dtype=str)
    df_rooms = pd.read_csv("data/rooms.csv", dtype=str)
    df_student_groups = pd.read_csv("data/student_groups.csv", dtype=str)
    df_hardblocks = pd.read_csv("data/hard_blocks.csv")
    df_accounts = pd.read_csv("data/accounts.csv")

    colors = list(range(0, 360, 10))
    random_colors = random.sample(colors, len(colors))

    for row in df_accounts.iterrows():
        hash_pass = bcrypt.generate_password_hash(str(row[1]['Password']))
        acc = Account(user=row[1]['User'], password=hash_pass,
                      role=row[1]['Role'], name=row[1]['Name'])
        db.session.add(acc)

    for index, row in df_professors.iterrows():
        prof = Professor(name=row['Name'], courses=row['Courses'],
                         colorCode=random_colors[index])
        db.session.add(prof)

    for index, row in df_courses.iterrows():
        course = Course(course=row['Course'], classes=row['Class'],
                        colorCode=random_colors[index])
        db.session.add(course)

    # for row in df_rooms.iterrows():
    #     room = Room(cc=row[1]['CC'], lec=row[1]['LEC'],
    #                 lab=row[1]['LAB'], tt=row[1]['TT'])
    #     db.session.add(room)

    for i in df_rooms.columns.tolist():
        for x in df_rooms[i].dropna().tolist():
            room = Room(name=i + x, req=i)
            db.session.add(room)

    for row in df_student_groups.iterrows():
        sg = StudentGroup(student_group=row[1]['Student Groups'],
                          courses=row[1]['Courses'])
        db.session.add(sg)

    for row in df_hardblocks.iterrows():
        hb = HardBlocks(day=row[1]["day"], period=row[1]["period"],
                        room=row[1]["room"],
                        reason=row[1]["reason"])
        db.session.add(hb)

    db.session.commit()


def existDB():
    """
    returns boolean value on whether database exists
    """
    import os
    return os.path.isfile('app.db')

def createTestDB(pathName):
    """
    Same as createDB but for testing purposes only
    """
    db.drop_all()
    db.create_all()

    df_professors = pd.read_csv(pathName+"professors.csv", dtype=str)
    df_courses = pd.read_csv(pathName+"courses.csv", dtype=str)
    df_rooms = pd.read_csv(pathName+"rooms.csv", dtype=str)
    df_student_groups = pd.read_csv(pathName+"student_groups.csv", dtype=str)
    df_hardblocks = pd.read_csv(pathName+"hard_blocks.csv")

    for row in df_professors.iterrows():
        prof = Professor(name=row[1]['Name'], courses=row[1]['Courses'])
        db.session.add(prof)

    for row in df_courses.iterrows():
        course = Course(course=row[1]['Course'], classes=row[1]['Class'])
        db.session.add(course)

    # for row in df_rooms.iterrows():
    #     room = Room(cc=row[1]['CC'], lec=row[1]['LEC'],
    #                 lab=row[1]['LAB'], tt=row[1]['TT'])
    #     db.session.add(room)

    for i in df_rooms.columns.tolist():
        for x in df_rooms[i].dropna().tolist():
            room = Room(name = i + x,req = i)
            db.session.add(room)

    for row in df_student_groups.iterrows():
        sg = StudentGroup(student_group=row[1]['Student Groups'],
                        courses=row[1]['Courses'])
        db.session.add(sg)


    for row in df_hardblocks.iterrows():
        hb = HardBlocks(day=row[1]["day"],period=row[1]["period"],
                        room =row[1]["room"],
                        reason = row[1]["reason"])
        db.session.add(hb)
    
    db.session.commit()

# if not existDB():
#     #if database does not exist we create it
#     createDB()

