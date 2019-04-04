class CourseClass:
    def __init__(self,course,req,duration):
        self.studentGroups = []
        self.course = course
        self.req = req
        self.duration = duration
        self.professors = []
        self.slots = []
       
        self.day = None
        self.startTime = None
        self.endTime = None
    def __repr__(self):
        return "<CourseClass:stg:{} course:{} req:{} duration:{}>".format(self.studentGroups,\
            self.course.name,self.req,self.duration)

    def addProf(self,prof):
        self.professors.append(prof)
    
    def appendStg(self):
        for stg in self.studentGroups:
            stg.courseClasses.append(self)
        