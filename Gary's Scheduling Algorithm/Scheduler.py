from Coordinator import Coordinator 
import random
import copy
def geneticScheduler(numberOfGen,popSize,tourSize,elitism=True):
    currPop = createInitialPop(popSize)
    #keep the best
    for i in range (numberOfGen-1):
        currPop = evolvePop(currPop,tourSize,elitism)

    return currPop


def evolvePop(currPop,tourSize,elitism =True):
    newPop = []
    tempPop = sorted(currPop,key = lambda coord : coord.fitnessValue)
    
    #save the best guy
    offset = 0
    if(elitism):
        newPop.append(tempPop[0])
        offset = 1
    for i in range(offset,len(tempPop)):
        
        parent1 = tournamentSel(tempPop,tourSize)
        parent2 = tournamentSel(tempPop,tourSize)
        
        child = mate(parent1,parent2)
        
        newPop.append(child)
    
    return newPop

def tournamentSel(currPop,tourSize):
    randomInt = random.randint(0,len(currPop)-1)
    fittest = currPop[randomInt]
    fitnessValue = fittest.fitnessValue 
    for i in range(tourSize-1):
        randomInt = random.randint(0,len(currPop)-1)
        if fittest.fitnessValue<fitnessValue:
            fitnessValue = fittest.fitnessValue
            fittest = currPop[randomInt]
    return fittest

def mate(c1,c2):
    #note take care to prevent alliasing issues
    
    c = Coordinator()
    c.generateRooms()
    c.generateSlots(True)
    c.generateCourses()
    c.generateProfs()
    c.generateStudentGroups()
    c.generateCourseClasses()

    for i in range(len(c1.courseClasses)):
        #we need to manage the professor and stg manually
        randomInt = random.randint(0,1)
        if(randomInt == 0):
            currCourseClass = c1.courseClasses[i]
        else:
            currCourseClass = c2.courseClasses[i]
       
        #from courseclass get stg, get prof, get slot and update values
        stgName = currCourseClass.studentGroup.name
        courseName = currCourseClass.course.name
        req = currCourseClass.req
        duration = currCourseClass.duration
        profNameList = [p.name for p in currCourseClass.professors]

        

    return c1

def mutate():
    pass

def createInitialPop(popSize):
    ls = []
    for _ in range(popSize):
        c = Coordinator()
        c.initalize()
        ls.append(c)
    return ls
import time
start = time.time()
lss = geneticScheduler(50,100,10)
print([f.fitnessValue for f in lss])
elasped = time.time() - start
print(elasped)