class Professor:
    
    def __init__(self,name):
        """course is list of course objects"""
        self.name = name
        self._course = []
        self.slots = []
    def addCourse(self,course):
        """adds Course Object to list"""
        self._course.append(course)
        course.professors.append(self)

    def addSlot(self,slot):
        self.slots.append(slot)
    
    #constraint prof cannot be at 2 places at any point in time
    def fitness(self):
        penatly = 0
        for s in range(len(self.slots)-1):
            for i in range(s+1,len(self.slots)):
                #if day and period is the same we add
                if self.slots[s].day == self.slots[i].day\
                    and self.slots[s].period == self.slots[i].period:
                    penatly +=1
        return penatly

    def __repr__(self):
        return"<Instructor:{},course:{}>".format(self.name,self._course)