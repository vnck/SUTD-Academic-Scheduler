class Professor:
    
    def __init__(self,name,course):
        """course is list of course objects"""
        self.name = name
        self.course = course
    
    def addCourse(self,course):
        self.course.append(course)

    def __repr__(self):
        return"<Instructor:{},course:{}>".format(self.name,self.course)