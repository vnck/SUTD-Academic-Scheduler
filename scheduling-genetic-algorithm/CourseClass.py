class CourseClass:
    def __init__(self, id, course, professorSize, professors, studentGroups, duration, classType=''):
        self.id = id
        self.course = course
        self.professorSize = professorSize
        self.professors = professors
        self.studentGroups = studentGroups
        self.duration = duration
        self.size = sum(studentGroup.size for studentGroup in studentGroups)
        self.classType = classType
