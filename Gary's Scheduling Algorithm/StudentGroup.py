class StudentGroup:
    def __init__(self,name):
        """
        attr:name,isFreshmore,course
        note course is a list of course objects
        """
        self.name = name
        if name[0:2] == "CC":
            self.isFreshmore = True
        else:
            self.isFreshmore = False
        self._course = []
        self.slots = []
        
    def addCourse(self,course):
        """adds course object"""
        self._course.append(course)

    def getCourses(self):
        return self._course

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
        return "<Student Group:{} Courses:{}>".format(self.name,self._course)