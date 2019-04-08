class CourseClass:
    def __init__(self,studentGroup,course,req,duration):
        self.studentGroup = studentGroup
        self.course = course
        
        if studentGroup.name[0:2]=="CC" and req =="CC":
            self.req = studentGroup.name
        else:
            self.req = req
        self.duration = duration
        self.professors = []
        self.slots = []
    def __repr__(self):
        return "<CourseClass:stg:{} course:{} req:{} duration:{}>".format(self.studentGroup.name,\
            self.course.name,self.req,self.duration)

    def addProf(self,prof):
        self.professors.append(prof)
        