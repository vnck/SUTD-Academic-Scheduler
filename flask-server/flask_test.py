from app import app, db, bcrypt
from flask import Flask, render_template, redirect, url_for, request
import sqlalchemy
from models import Account, Professor, Course, CourseCoordinator, Room, StudentGroup, CourseClass
# Adding Courses
mycourse = Course(name="math")
mycourse2 = Course(name="science")

# Adding Professors/Course Coordinators
myprof = Professor(name="JJ", initials="j", hash_pass=bcrypt.generate_password_hash(
    'hunter2'), courses=[mycourse])
myprof2 = Professor(name="GG", initials="G", hash_pass=bcrypt.generate_password_hash(
    'gg'), courses=[mycourse, mycourse2])
mycourseco = CourseCoordinator(
    name="cc", initials="c", hash_pass=bcrypt.generate_password_hash('cc'))

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
db.session.commit()

# Test accounts/Professors and CourseCoordinators
print("Test Accounts")
acc2 = Account.query.all()
# Example of how to get an Account object from database
profacc = Account.query.filter_by(name="JJ").first()
print(acc2)

# Test courses
print("Test Courses")
print(Course.query.all())

# Test rooms
print("Test rooms")
print(Room.query.all())

# Test Student Groups
print("Test Student Groups")
print(StudentGroup.query.all())

# Test CourseClass
print("Test Course Class")
print(CourseClass.query.all())

# use decorators to link the function to a url


@app.route('/')
def home():
    return "Hello, World!"  # return a string


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        acc = Account.query.filter_by(name=request.form['username']).first()
        if acc == None:
            error = 'Invalid Credentials. Please try again.'
        elif bcrypt.check_password_hash(acc.hash_pass, request.form['password']) == False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('welcome.html', error=error)  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

# Route for handling the login page logic
