from Coordinator import Coordinator 
import random
import copy
Coordinator.initalizeStatic()
def geneticScheduler(numberOfGen,popSize,tourSize,elitism=True):
    currPop = createInitialPop(popSize)
    #keep the best
    for i in range (numberOfGen-1):
        print("iter {}".format(i))
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
        print(parent1.fitnessValue)
        print(parent2.fitnessValue)
        child = mate(parent1,parent2)
        print("child fit {}".format(child.fitnessValue))
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
        #copying courseClasses attributes no alliasing
        c.courseClasses[i].studentGroup = c.getSTG(stgName)
        c.courseClasses[i].course = c.getCourse(courseName)
        c.courseClasses[i].req = req
        c.courseClasses[i].duration = duration
        
        for name in profNameList:
            c.courseClasses[i].professors.append(c.getProf(name))
        
        for slot in currCourseClass.slots:
            index = slot.index
            c.slots[index].counter += 1
            c.courseClasses[i].studentGroup.slots.append(c.slots[index])
            c.courseClasses[i].slots.append(c.slots[index])
            for prof in c.courseClasses[i].professors:
                prof.slots.append(c.slots[index])

        c.solution[c.courseClasses[i]] = c.slots[index]
    c.fitness()
    
    print(c.studentGroups)
    return c

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
lss = geneticScheduler(100,100,20)
print([f.fitnessValue for f in lss])
elasped = time.time() - start
print(elasped)