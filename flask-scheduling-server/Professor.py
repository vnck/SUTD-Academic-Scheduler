class Professor:

    def __init__(self, name):
        """course is list of course objects"""
        self.name = name
        self._course = []
        self.slots = []
        self.courseClasses = []

        # list of tuples
        self.requests = []

        self.penalty = 0

        self.satisfied = False

    def addCourse(self, course):
        """adds Course Object to list"""
        self._course.append(course)
        course.professors.append(self)

    def addSlot(self, slot):
        self.slots.append(slot)

    # constraint prof cannot be at 2 places at any point in time
    def fitness(self):
        penalty = 0
        for s in range(len(self.slots)-1):
            for i in range(s+1, len(self.slots)):
                # if day and period is the same we add
                if self.slots[s].day == self.slots[i].day\
                        and self.slots[s].period == self.slots[i].period:
                    penalty += 1

        self.satisfied = True
        for tupl in self.requests:
            day = float(tupl[0])
            startTime = float(tupl[1])
            endTime = float(tupl[2])
            if startTime != None and endTime != None and day != None:
                for slot in self.slots:
                    if float(slot.day) == day:
                        if float(slot.period) <= endTime and float(slot.period) >= startTime:
                            penalty += 0.1
                            self.satisfied = False
                            break
        # check soft constraints
        # if self.startTime != None and self.endTime != None and self.day != None:
        #     for slot in self.slots:
        #         if slot.day == self.day:
        #             if slot.period<=self.endTime and slot.period>= self.startTime:
        #                 #penalise once
        #                 penalty+=0.01
        #                 break
        self.penalty = penalty
        return penalty

    def __repr__(self):
        return"<Instructor:{},course:{}>".format(self.name, self._course)
