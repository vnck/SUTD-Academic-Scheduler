from Coordinator import Coordinator 
import random
import copy
Coordinator.initalizeStatic()
def geneticScheduler(numberOfGen,popSize,tourSize,mutateRate=0.05,elitismOffset=1):
    currPop = createInitialPop(popSize)
    #keep the best
    for i in range (numberOfGen-1):
        if(currPop[0].fitnessValue==0):break
        print("iter {}".format(i))
        currPop = evolvePop(currPop,tourSize,mutateRate,elitismOffset)
        
    return currPop


def evolvePop(currPop,tourSize,mutateRate=0.05,elitismOffset=1):
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
            
            c.solution[c.slots[index]] = c.courseClasses[i]


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
                cc.studentGroup.slots.remove(slot)
                try:
                    del c1.solution[slot]
                except KeyError:
                    #key already removed so dont need to do anything
                    pass
                for prof in cc.professors:
                    prof.slots.remove(slot)
            cc.professors.clear()
            cc.slots.clear()
            
            duration = cc.duration
            randDay = random.randint(0,NUM_DAYS-1)

            checker = True
            for roomNum in range(NUM_ROOMS):
                
                if c1.slots[roomNum].getReq() == cc.req and checker:
                    randRoomStart = roomNum
                    checker = False
                if c1.slots[roomNum].getReq() != cc.req and not checker: 
                    randRoomEnd = roomNum - 1
                    break
                if  roomNum == NUM_ROOMS-1:
                    randRoomEnd = roomNum
            #print((randRoomStart,randRoomEnd))
            randRoom = random.randint(randRoomStart,randRoomEnd)
            #randRoom = random.randint(0,NUM_ROOMS-1)
            
            #makes sure that same lesson does not go on to the next day
            randPeriod = random.randint(0,NUM_PERIODS-1-int((duration-0.5)/0.5))
            randProf = random.choice(cc.course.professors)
            cc.professors.append(randProf)
            for i in range(int(duration/0.5)):
                position = randDay*NUM_ROOMS*NUM_PERIODS + (randPeriod+i)*NUM_ROOMS + randRoom
                # store the schedule for student groups and professors in a slot[]
                cc.studentGroup.slots.append(c1.slots[position])
                cc.slots.append(c1.slots[position])
                randProf.slots.append(c1.slots[position])
                c1.solution[c1.slots[position]] = cc
                c1.slots[position].counter += 1
            
def createInitialPop(popSize):
    ls = []
    for _ in range(popSize):
        c = Coordinator()
        c.initalize()
        ls.append(c)
    return ls
import time
start = time.time()
lss = geneticScheduler(100,100,5,elitismOffset=5,mutateRate=0.05)
print([f.fitnessValue for f in lss])
elasped = time.time() - start
print(elasped)

answer = sorted(lss,key = lambda coord : coord.fitnessValue)[0]

for prof in answer.professors:
    print(prof.name)
    for slot in prof.slots:
        print(slot,answer.solution[slot])
# profName = input("Get schedule for professor:")
# prof = answer.getProf(profName)
# print(prof.slots)