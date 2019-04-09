class StudentGroup:
    def __init__(self, name):
        """
        attr:name,course
        note course is a list of course objects
        """
        self.name = name
        self._course = []
        self.slots = []

        self.courseClasses = []

    def addCourse(self, course):
        """adds course object"""
        self._course.append(course)
        # adds student groups to course object
        course.studentGroups.append(self)

    def getCourses(self):
        return self._course

    def fitness(self):
        penalty = 0
        # check time space constraints
        for s in range(len(self.slots)-1):
            for i in range(s+1, len(self.slots)):
                # if day and period is the same we add
                if self.slots[s].day == self.slots[i].day\
                        and self.slots[s].period == self.slots[i].period:
                    penalty += 1

        # Check that no two of the same course in a single day
        # cannot have the same subject twice in a single day
        for i in range(len(self.courseClasses)-1):
            for j in range(s+1, len(self.courseClasses)):
                if self.courseClasses[i].day == self.courseClasses[j].day\
                        and self.courseClasses[i].course == self.courseClasses[j].course:
                    penalty += 1
        return penalty

    def __repr__(self):
        return "<Student Group:{} Courses:{} Slots:{}>".format(self.name, self._course, len(self.slots))
