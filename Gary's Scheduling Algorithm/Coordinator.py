from Slot import Slot
from Room import Room
from Course import Course
from Professor import Professor
import InputUtils
import pandas as pd
class Coordinator:
    def __init__(self):
        self.days = [1,2,3,4,5]
        self.periods = self._generate_periods()
        self.rooms = []
        self.slots = []
        self.courses = []
        self.professors = []
        self.studentGroups = []

    def getCourse(self,name):
        """returns course object from courses with given name"""
        for course in self.courses:
            if name == course.name:
                return course
        return None
    # def generateProfs(self):
    #     """
    #     for now assume instructor only teaches one course
    #     """
    #     df = InputUtils.readProfCSV()
    #     for i,row in df.iterrows():
    #         instructorList = row[1].split(",")
    #         for inst in instructorList:
    #             courseName = row[1]
    #             course = self.getCourse(courseName)
    #             self.professors.append(Professor(inst,[course]))

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
print(c.professors)
print(c.courses)