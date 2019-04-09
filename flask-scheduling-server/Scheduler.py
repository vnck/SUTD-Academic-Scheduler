from Coordinator import Coordinator 
import random
import copy
import models
import time
import models
from app import db

running = False

def geneticScheduler(numberOfGen,popSize,tourSize,mutateProb = 0.5,mutateRate=0.05,elitismOffset=1):
    """
    parameters \n
    number of generations/iterations \n
    population size \n
    tournament size:for mating select random sample of tournameSize and choose the best \n
    mutateProb: probability of those who mate to mutate \n
    mutateRate:probability of genes to be mutated \n
    elitismOffset: selects the best handful to keep for the next generation
    """
    currPop = createInitialPop(popSize)
    #keep the best
    for i in range (numberOfGen-1):
        if(currPop[0].fitnessValue<=0.001):break
        print("iter {}".format(i))
        currPop = evolvePop(currPop,tourSize,mutateProb,mutateRate,elitismOffset)
        
    return currPop


def evolvePop(currPop,tourSize,mutateProb=0.5,mutateRate=0.05,elitismOffset=1):
    newPop = []
    
    tempPop = sorted(currPop,key = lambda coord : coord.fitnessValue)
    #save the best guy
    print(tempPop[0].fitnessValue," penalty prof:{} stg:{} slot:{} req:{}".format(tempPop[0].profPenalty\
        ,tempPop[0].stgPenalty,tempPop[0].slotPenalty,tempPop[0].reqPenalty))
    for j in range (elitismOffset):
        newPop.append(tempPop[j])
    
    for i in range(elitismOffset,len(tempPop)):
        parent1 = tournamentSel(tempPop,tourSize)
        parent2 = tournamentSel(tempPop,tourSize)
        #print(parent1.fitnessValue)
        #print(parent2.fitnessValue)
        child = mate(parent1,parent2)
        if random.random()<mutateProb:
            mutate(child,mutateRate)
        child.fitness()
        #print("child fit {}".format(child.fitnessValue))
        newPop.append(child)
        
    return newPop

def tournamentSel(currPop,tourSize):
    randomInt = random.randint(0,len(currPop)-1)
    fittest = currPop[randomInt]
    fitnessValue = fittest.fitnessValue 
    for i in range(tourSize-1):
        randomInt = random.randint(0,len(currPop)-1)
        currFit = currPop[randomInt]
        if currFit.fitnessValue<fitnessValue:
            fitnessValue = currFit.fitnessValue
            fittest = currFit
    return fittest

def mate(c1,c2):
    #note take care to prevent alliasing issues
    c = Coordinator()
    c.generateSlots()
    c.generateCourses()
    c.generateProfs()
    c.assignRequests()
    c.generateStudentGroups()
    c.generateCourseClasses()
    c.appendSTGtoCC()
    c.setHardBlocks()


    for i in range(len(c1.courseClasses)):
        #we need to manage the professor and stg manually
        randomInt = random.randint(0,1)
        if(randomInt == 0):
            currCourseClass = c1.courseClasses[i]
        else:
            currCourseClass = c2.courseClasses[i]
       
        #from courseclass get stg, get prof, get slot and update values
        courseName = currCourseClass.course.name
        req = currCourseClass.req
        duration = currCourseClass.duration
        
        day = currCourseClass.day
        startTime = currCourseClass.startTime
        endTime = currCourseClass.endTime

        profNameList = [p.name for p in currCourseClass.professors]
        #copying courseClasses attributes no alliasing
        c.courseClasses[i].course = c.getCourse(courseName)
        c.courseClasses[i].req = req
        c.courseClasses[i].duration = duration
        c.courseClasses[i].day = day
        c.courseClasses[i].startTime = startTime
        c.courseClasses[i].endTime = endTime
    
        for name in profNameList:
            c.courseClasses[i].professors.append(c.getProf(name))
        
        
        for prof in c.courseClasses[i].professors:
            prof.courseClasses.append(c.courseClasses[i])

        for slot in currCourseClass.slots:
            index = slot.index
            c.slots[index].counter += 1
            c.courseClasses[i].slots.append(c.slots[index])
            for stg in c.courseClasses[i].studentGroups:
                stg.slots.append(c.slots[index])
                
            for prof in c.courseClasses[i].professors:
                prof.slots.append(c.slots[index])
            


    return c

def mutate(c1,mutateRate):
    NUM_DAYS = len(c1.days)
    NUM_ROOMS = len(Coordinator.rooms)
    NUM_PERIODS = len(Coordinator.periods)
    
    for cc in c1.courseClasses:
        #shift a course class somewhere else
        if(random.random()<mutateRate):
            for slot in cc.slots:
                #remove class from allocated slot slot.counter -=1
                slot.counter-=1
                for stg in cc.studentGroups:
                    stg.slots.remove(slot)
                for prof in cc.professors:
                    prof.slots.remove(slot)

            for prof in cc.professors:
                prof.courseClasses.remove(cc)
            cc.professors.clear()
            cc.slots.clear()
        
            
            #rerandom courseclass
            c1.randomizeCourseClass(cc,NUM_DAYS,NUM_ROOMS,NUM_PERIODS)
            
def createInitialPop(popSize):
    ls = []
    for _ in range(popSize):
        c = Coordinator()
        c.initalize()
        ls.append(c)
    return ls

def startAlgo():
    print("Initializing and reading from db")
    Coordinator.initalizeStatic()
    print("Algorithm starts")
    start = time.time()
    lss = geneticScheduler(1000,100,5,mutateProb=0.8,elitismOffset=5,mutateRate=0.05)
    print([f.fitnessValue for f in lss])
    elasped = time.time() - start
    print("time taken = {}s".format(elasped))
    answer = sorted(lss,key = lambda coord : coord.fitnessValue)[0]
    if answer.fitnessValue > 1: raise Exception("Hard Constraints not Satisfied")
    #key into database
    #deletes all previous data
    models.CourseClass.query.delete()

    for cc in answer.courseClasses:
        stgString = cc.studentGroups[0].name
        profString = cc.professors[0].name
        
        for i in range(1,len(cc.studentGroups)):
            stgString += ",{}".format(cc.studentGroups[i].name)

        for j in range(1,len(cc.studentGroups)):
            profString += ",{}".format(cc.professors[j].name)
        
        day = cc.day
        startTime = cc.startTime
        endTime = cc.endTime
        roomName = cc.slots[0].room.name
        courseName = cc.course.name
        courseClassDb = models.CourseClass(course=courseName,studentGroups = stgString,professors = profString,
                                            day = day,startTime= startTime,endTime = endTime,room= roomName)
        db.session.add(courseClassDb)
    
    #adding soft constraints
    for prof in answer.professors:
        name = prof.name
        if prof.penalty>0:
            a = False
        else:
            a = True
        
        currProf = models.Professor.query.filter(models.Professor.name == name).first()
        currProf.satisfied = a
        
        
    db.session.commit()


if __name__ == "__main__":
    if not models.existDB():
        models.createDB()
    
    startAlgo()

    for cc in models.CourseClass.query.all():
        print(cc)

#TODO 
#1 DONE:implement lecture all student groups all profs
    #change the courseclass to have a stg array
    #so a lecture class is only 1 course class
#2 DONE:implement time blocks such as HASS/5th rows
    #in Slot class hardBlock
#3 DONE:implement soft constraints
    #add it into the professor class and change the prof fitness function
#4 implement output db
#5 DONE:implement student groups cannot have more than 1 lesson of the same course
    
