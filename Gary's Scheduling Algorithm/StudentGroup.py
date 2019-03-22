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

    def __repr__(self):
        return "<Student Group:{} Courses:{}>".format(self.name,self._course)