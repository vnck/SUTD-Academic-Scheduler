import models
from CourseClass import CourseClass
from app import db
import numpy as np
import xlsxwriter
import csv
import pandas as pd
from ics import Calendar, Event
import arrow


def makeICS(courseClasses, name):

    slots = ['08:30:00', '09:00:00', '09:30:00', '10:00:00',
             '10:30:00', '11:00:00', '11:30:00', '12:00:00',
             '12:30:00', '13:00:00', '13:30:00', '14:00:00',
             '14:30:00', '15:00:00', '15:30:00', '16:00:00',
             '16:30:00', '17:00:00', '17:30:00', '18:00:00']

    days = ['2019-04-08 ', '2019-04-09 ',
            '2019-04-10 ', '2019-04-11 ', '2019-04-12 ']

    c = Calendar()
    for courseClass in courseClasses:
        courseName = courseClass.course  # String
        studentGroups = courseClass.studentGroups  # String
        professors = courseClass.professors  # String
        day = courseClass.day  # Int
        room = courseClass.room  # String
        startTime = int((courseClass.startTime - 8.5) / 0.5)
        endTime = int((courseClass.endTime - 8.5) / 0.5)

        e = Event(name=courseName, description=professors, location=room)

        d1 = arrow.get(days[day-1] + slots[startTime], 'YYYY-MM-DD HH:mm:ss')
        d2 = arrow.get(days[day-1] + slots[endTime], 'YYYY-MM-DD HH:mm:ss')
        e.begin, e.end = d1, d2

        c.events.add(e)
  #		if courseName == "50.034":
  #			c.events.add(e)
  #			count += 1
  #		else:
  #			count += 1
        print(c.events)
        open('files/schedule-' + name + '.ics', 'w').writelines(c)


def makeCSV(courseClasses, name):
    slots = [
        '08:30 AM', '09:00 AM', '09:30 AM', '10:00 AM',
        '10:30 AM', '11:00 AM', '11:30 AM', '00:00 PM',
        '00:30 PM', '01:00 PM', '01:30 PM', '02:00 PM',
        '02:30 PM', '03:00 PM', '03:30 PM', '04:00 PM',
        '04:30 PM', '05:00 PM', '05:30 PM', '06:00 PM'
    ]
    days = ['04/08/2019', '04/09/2019',
            '04/10/2019', '04/11/2019', '04/12/2019']
    colNames = ["Subject", "Start Date", "Start Time",
                "End Date", "End Time", "Description", "Location"]

    with open('files/schedule-' + name + '.csv', 'w', newline='') as csvfile:
        fieldnames = colNames
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for courseClass in courseClasses:

            courseName = courseClass.course
            studentGroups = courseClass.studentGroups
            professors = courseClass.professors
            day = courseClass.day
            room = courseClass.room
            startTime = int((courseClass.startTime - 8.5) / 0.5)
            endTime = int((courseClass.endTime - 8.5) / 0.5)

            content = "Professor: " + professors + ", Students: " + studentGroups

            writer.writerow({'Subject': courseName, 'Start Date': days[day-1], 'Start Time': slots[startTime],
                             'End Date': days[day-1], 'End Time': slots[endTime], 'Description': content, 'Location': room})
