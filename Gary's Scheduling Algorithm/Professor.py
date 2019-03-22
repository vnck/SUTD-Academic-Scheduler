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
    def __repr__(self):
        return"<Instructor:{},course:{}>".format(self.name,self._course)