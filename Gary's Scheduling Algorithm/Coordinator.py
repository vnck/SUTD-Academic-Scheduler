from Slot import Slot
from Room import Room
from Course import Course
from Professor import Professor
from StudentGroup import StudentGroup
from CourseClass import CourseClass

import InputUtils
import pandas as pd
import random

class Coordinator:
    def __init__(self):
        self.days = [1,2,3,4,5]
        self.periods = self._generate_periods()
        self.rooms = []
        self.slots = []
        self.courses = []
        self.professors = []
        self.studentGroups = []
        self.courseClasses = []
        self.solution = None

    def fitness(self):
        pass

    def generateOneRandSolution(self):
        
        NUM_DAYS = len(self.days)
        NUM_ROOMS = len(self.rooms)
        NUM_PERIODS = len(self.periods)

        solution = {}
        for courseClass in self.courseClasses:
            #get the duration for the class
            duration = courseClass.duration

            #generate random day,num,periods
            randDay = random.randint(0,NUM_DAYS-1)
            randRoom = random.randint(0,NUM_ROOMS-1)
            
            #makes sure that same lesson does not go on to the next day
            randPeriod = random.randint(0,NUM_PERIODS-1-int((duration-0.5)/0.5))
            
            #get random prof teaching the class
            #guarantees that the prof teaches the class
            randProf = random.choice(courseClass.course.professors)
            courseClass.professors.append(randProf)
            
            #get the slots position from the random values
            for i in range(int(duration/0.5)):
                position = randDay*NUM_ROOMS*NUM_PERIODS + (randPeriod+i)*NUM_ROOMS + randRoom
                # store the schedule for student groups and professors in a slot[]
                courseClass.studentGroup.slots.append(self.slots[position])
                randProf.slots.append(self.slots[position])

            solution[courseClass] = self.slots[position]

        self.solution = solution

    def getCourse(self,name):
        """returns course object from courses with given name"""
        for course in self.courses:
            if name == course.name:
                return course
        return None

    def generateCourseClasses(self):
        for stg in self.studentGroups:
            for course in stg.getCourses():
                for req,duration in course.getClasses():
                    c = CourseClass(stg,course,req,duration)
                    self.courseClasses.append(c)
                
    def generateStudentGroups(self):
        df = InputUtils.readStgCSV()
        for i,row in df.iterrows():
            stg = row[0]
            courses = row[1].split(",")
            studentGroup = StudentGroup(stg)
            for course in courses:
                courseObject = self.getCourse(str(course))
                if(courseObject==None): raise Exception("Course {} not found".format(course))
                studentGroup.addCourse(courseObject)
            self.studentGroups.append(studentGroup)

    def generateProfs(self):
        """
        for now assume instructor only teaches one course
        """
        df = InputUtils.readProfCSV()
        for i,row in df.iterrows():
            inst = row[0]#instructor
            courseCode = str(round(row[1],3))
            course = self.getCourse(courseCode)
            p = Professor(inst)
            p.addCourse(course)
            self.professors.append(p)

    def generateCourses(self):
        for dict in InputUtils.getStudentGroupData():
            course = Course(dict["subjectCode"])
            check = True
            for c in self.courses:
                if c.name == course.name:
                    check = False
            if check:
                for i in dict["classes"]:
                    if i[0]=="CBL":
                        course.addClass("CC",i[1])
                     
                    elif i[0]== "LEC":
                        course.addClass("LEC",i[1])
                self.courses.append(course)

    def generateRooms(self):
        dict = InputUtils.readRoomCSV()
        for k in dict.keys():
            for v in dict[k]:
                self.rooms.append(Room(v,k))

    def generateSlots(self,boolSort):
        """
        for space time constraints
        """
        for days in self.days:
            for periods in self.periods:
                for rooms in self.rooms:
                    self.slots.append(Slot(days,periods,rooms))
                    
    def _generate_periods(self):
        x = 8.5
        lsToReturn = []
        lsToReturn.append(x)
        for _ in range(18):
            x+=0.5
            lsToReturn.append(x)
        return lsToReturn

    def setDaysList(self,ls):
        """
        setting days if different from default
        """
        self.days = ls
    
    def setPeriodsList(self,ls):
        """
        setting days if different from default
        """
        self.periods = ls


c = Coordinator()
c.generateRooms()
c.generateSlots(True)
c.generateCourses()
c.generateProfs()
c.generateStudentGroups()
c.generateCourseClasses()
#print(c.courseClasses)
print(len(c.slots))
print(c.solution)
#print(len(c.slots))
#print(c.professors)
#print(c.courses)
#print(c.studentGroups)
#print(c.slots)