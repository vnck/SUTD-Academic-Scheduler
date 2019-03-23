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
    rooms = []
    periods = []
    def __init__(self):
        self.days = [1,2,3,4,5]
        self.slots = []
        self.courses = []
        self.professors = []
        self.studentGroups = []
        self.courseClasses = []
        self.solution = {}
        #lower fitnessValue is better
        self.fitnessValue = None

        #debugging
        self.profPenalty = 0
        self.stgPenalty = 0
        self.slotPenalty = 0
        self.reqPenalty = 0
    
        
    def fitness(self):
        #instructor cannot be at more than 1 room per day per period
        # print("prof len {}".format(len(self.professors)))
        # print("stg len {}".format(len(self.studentGroups)))
        # print("slot len {}".format(len(self.slots)))
        # print("dict len {}".format(len(self.solution.keys())))
        penalty = 0
        for prof in self.professors:
            penalty+=prof.fitness()
        self.profPenalty = penalty
        # #student group cannot be at more than 1 day per room per period
        for stg in self.studentGroups:
            penalty+= stg.fitness()
        self.stgPenalty = penalty - self.profPenalty
        # each room can only be used once per period per day
        for slot in self.slots:
            if (slot.counter-1<0):
                count = 0
            else:
                count = slot.counter-1
            penalty+=count
        self.slotPenalty = penalty - self.profPenalty - self.stgPenalty

        # #check if room meets requirements
        # for courseClass,slot in self.solution.items():
        #     if courseClass.req != slot.room.req:
        #         penalty += 1
        #     #freshmore need to use their own class
        #     elif courseClass.studentGroup.isFreshmore:
        #         courseClass.studentGroup.name != slot.room.name
        #         penalty+=1
        # self.reqPenalty = penalty - self.slotPenalty - self.profPenalty - self.stgPenalty
        self.fitnessValue = penalty
        return penalty

    def generateOneRandSolution(self):
        
        NUM_DAYS = len(self.days)
        NUM_ROOMS = len(Coordinator.rooms)
        NUM_PERIODS = len(Coordinator.periods)


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
                courseClass.slots.append(self.slots[position])
                randProf.slots.append(self.slots[position])
                self.slots[position].counter += 1

            self.solution[courseClass] = self.slots[position]

     
    
    def getProf(self,name):
        for prof in self.professors:
            if prof.name == name:
                return prof
        return None

    def getSTG(self,name):
        for stg in self.studentGroups:
            if stg.name == name:
                return stg
        return None
    
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
            p = Professor(inst)
            for courseCode in row[1].split(","):
                course = self.getCourse(courseCode)
                p.addCourse(course)
            self.professors.append(p)

    def generateCourses(self):
        df = InputUtils.readCourseCSV()
        for i,row in df.iterrows():
            name = str(round(row[0],3))
            course = Course(name)
            arr = row[1].split(",")
            for c in arr:
                req = c[0:c.find("(")]
                duration = float(c[c.find("(")+1:c.find(")")])
                course.addClass(req,duration)
            self.courses.append(course)
    
    @staticmethod
    def generateRooms():
        dict = InputUtils.readRoomCSV()
        for k in dict.keys():
            for v in dict[k]:
                Coordinator.rooms.append(Room(v,k))

    def generateSlots(self,boolSort):
        """
        for space time constraints
        """
        index = 0
        for days in self.days:
            for period in Coordinator.periods:
                for rooms in Coordinator.rooms:
                    s = Slot(days,period,rooms)
                    self.slots.append(s)
                    s.index = index
                    index += 1
    @staticmethod           
    def _generate_periods():
        x = 8.5
        Coordinator.periods.append(x)
        for _ in range(18):
            x+=0.5
            Coordinator.periods.append(x)
        

    def setDaysList(self,ls):
        """
        setting days if different from default
        """
        self.days = ls
    
    def setPeriodsList(self,ls):
        """
        setting days if different from default
        """
        Coordinator.periods = ls

    def initalize(self):
        #to consider separate generation of rooms/courses separately to decrease time complexity
        self.generateSlots(True)
        self.generateCourses()
        self.generateProfs()
        self.generateStudentGroups()
        self.generateCourseClasses()
        self.generateOneRandSolution()
        self.fitness()

    @staticmethod
    def initalizeStatic():
        Coordinator._generate_periods()
        Coordinator.generateRooms()

# Coordinator.initalizeStatic()
# c = Coordinator()
# c.initalize()
# print(c.studentGroups)

# c.generateRooms()
# c.generateSlots(True)
# c.generateCourses()
# c.generateProfs()
# c.generateStudentGroups()
# c.generateCourseClasses()
# c.generateOneRandSolution()
# c.fitness()


# print(len(c.slots))
# print(c.solution)
#print(len(c.slots))
#print(c.professors)
#print(c.courses)
#print(c.studentGroups)
#print(c.slots)