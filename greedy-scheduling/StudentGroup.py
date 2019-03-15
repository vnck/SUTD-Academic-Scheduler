class StudentGroup:
    def __init__(self, key, label, term, code, size):
        self.key = key
        self.label = label
        self.term = term
        self.subjectCode = code
        self.size = size
        self.day = -1
        self.period = -1
        self.noClash = False
        self.classes = []
        self.venues = []
        self.avail = []
    
    def AddTimeSlot(self,day,period):
        self.avail.append((day,period))

    def checkAvail(self,day,period):
        for tupl in self.avail:
            if day == tupl[0] and period == tupl[1]:
                return False
        return True
    def addTimeDateConstraint(self, day, period, noClash=False):
        self.day = day
        self.period = period
        self.noClash = noClash

    def addClasses(self, classes):
        self.classes = classes

    def addVenues(self, venues):
        self.venues = venues

    def print_summary(self):
        print('SG: {}, label: {}, size: {}, classes: {}, venues: {}'.format(
            self.key, self.label, self.size, self.classes, self.venues))
    def __repr__(self):
        return 'SG: {}, label: {}, size: {}, classes: {}, venues: {}'.format(
            self.key, self.label, self.size, self.classes, self.venues)
