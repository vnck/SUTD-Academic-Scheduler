from Slot import Slot
from Room import Room
from Course import Course
from Professor import Professor
from StudentGroup import StudentGroup
from CourseClass import CourseClass

#for database integration
import models

import InputUtils
import pandas as pd
import random

class Coordinator:
    rooms = []
    periods = []
    coursesDb = []
    profDb = []
    stgDb = []
    hardBlocksDb = []
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
            if slot.counter>=1 and slot.hardBlock:
                penalty += 1
            penalty+=count
        self.slotPenalty = penalty - self.profPenalty - self.stgPenalty

        # #check if room meets requirements
        for slot,courseClass in self.solution.items():
            #print(courseClass.req,slot.getReq())
            if courseClass.req != slot.getReq():
                penalty += 1
                #print(courseClass.req,slot.getReq())
                raise Exception("course class {} does not meet req {}".format(courseClass.req,slot.room.req))
        
        self.reqPenalty = penalty - self.slotPenalty - self.profPenalty - self.stgPenalty
        self.fitnessValue = penalty
        return penalty

    def generateOneRandSolution(self):
        
        NUM_DAYS = len(self.days)
        NUM_ROOMS = len(Coordinator.rooms)
        NUM_PERIODS = len(Coordinator.periods)


        for courseClass in self.courseClasses:
            self.randomizeCourseClass(courseClass,NUM_DAYS,NUM_ROOMS,NUM_PERIODS)    

     
    def randomizeCourseClass(self,courseClass,NUM_DAYS,NUM_ROOMS,NUM_PERIODS):
        #get the duration for the class
        duration = courseClass.duration

        #generate random day,num,periods
        randDay = random.randint(0,NUM_DAYS-1)
        # print(NUM_ROOMS)
           
    
        checker = True
        for roomNum in range(NUM_ROOMS):
      
                
            if self.slots[roomNum].getReq() == courseClass.req and checker:
                randRoomStart = roomNum
                checker = False
                
            if self.slots[roomNum].getReq() != courseClass.req and not checker:
                randRoomEnd = roomNum - 1
                break

            if roomNum == NUM_ROOMS - 1:
                randRoomEnd = roomNum
            
        if(self.slots[randRoomStart].getReq()!= self.slots[randRoomEnd].getReq()):raise Exception("random rooms does not meet req")
        randRoom = random.randint(randRoomStart,randRoomEnd)
            
        #makes sure that same lesson does not go on to the next day
        randPeriod = random.randint(0,NUM_PERIODS-1-int((duration-0.5)/0.5))
            
        #get random prof teaching the class
        #guarantees that the prof teaches the class
        if courseClass.req == "LEC":
            for prof in courseClass.course.professors:
                courseClass.professors.append(prof)
        else:
            randProf = random.choice(courseClass.course.professors)
            courseClass.professors.append(randProf)
            
        #get the slots position from the random values
        for i in range(int(duration/0.5)):
            position = randDay*NUM_ROOMS*NUM_PERIODS + (randPeriod+i)*NUM_ROOMS + randRoom
            # store the schedule for student groups and professors in a slot[]

            for stg in courseClass.studentGroups:
                stg.slots.append(self.slots[position])
            courseClass.slots.append(self.slots[position])
            for prof in courseClass.professors:
                prof.slots.append(self.slots[position])
            self.solution[self.slots[position]] = courseClass
            self.slots[position].counter += 1

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
        for course in self.courses:
            for req,duration in course.getClasses():
                if req == "LEC":
                    c = CourseClass(course,req,duration)
                for stg in course.studentGroups:
                    if req != "LEC":
                        if req == "CC" and stg.name[0:2] == "CC":
                            #if it is cohort class we set the req to the class name
                            c = CourseClass(course,stg.name,duration)
                        else:
                            c = CourseClass(course,req,duration)
                        c.studentGroups.append(stg)
                        self.courseClasses.append(c)
                    elif req =="LEC":
                        c.studentGroups.append(stg)
                if req =="LEC":
                    self.courseClasses.append(c)


                
    def generateStudentGroups(self):
        stgs = Coordinator.stgDb
        for stg in stgs:
            name = stg.student_group
            studentGroup = StudentGroup(name)
            for course in stg.courses.split(","):
                courseObject = self.getCourse(course)
                if(courseObject==None): raise Exception("Course {} not found".format(course))
                studentGroup.addCourse(courseObject)
            self.studentGroups.append(studentGroup)

    def generateProfs(self):
        profs = Coordinator.profDb
        for prof in profs:
            name = prof.name
            p = Professor(name)
            #setting soft constraints
            p.day = prof.day
            p.startTime = prof.startTime
            p.endTime = prof.endTime
            
            for courseCode in prof.courses.split(","):
                course = self.getCourse(courseCode)
                p.addCourse(course)
            self.professors.append(p)
    
    def generateCourses(self):
        courses = Coordinator.coursesDb
        for cour in courses:
            name = cour.course
            classes = (cour.classes).split(",")
            course = Course(name)
            for c in classes:
                req = c[0:c.find("(")]
                duration = float(c[c.find("(")+1:c.find(")")])
                course.addClass(req,duration)
            self.courses.append(course)
    
    @staticmethod
    def generateRooms():
        """copy data from db into ram"""
        rooms = models.Room.query.all()
        for room in rooms:
            name = room.name
            req = room.req
            Coordinator.rooms.append(Room(name,req))

   
    

    def generateSlots(self):
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
    
    def setHardBlocks(self):
        for hb in Coordinator.hardBlocksDb:
            for slot in self.slots:
                if hb.room == "all":
                    if slot.day == hb.day and slot.period == hb.period:
                        slot.hardBlock = True
                elif hb.room == slot.room.name and slot.day == hb.day and slot.period == hb.period:
                    
                    slot.hardBlock = True
             
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
        self.generateSlots()
        self.generateCourses()
        self.generateProfs()
        self.generateStudentGroups()
        self.generateCourseClasses()
        self.setHardBlocks()
        self.generateOneRandSolution()
        self.fitness()

    @staticmethod
    def initalizeStatic():
        Coordinator._generate_periods()
        Coordinator.generateRooms()
        Coordinator.coursesDb = models.Course.query.all()
        Coordinator.profDb = models.Professor.query.all()
        Coordinator.stgDb = models.StudentGroup.query.all()
        Coordinator.hardBlocksDb = models.HardBlocks.query.all()

