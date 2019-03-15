class Slot:
    def __init__(self, day, period,venue):
        self.day = day
        self.period = period
        self.venue = venue
        self.studentGroups = []
        self.instructor = []
        self._isOccupied = False
    def __repr__(self):
        return"<Slot:day={0},period={1},studentgroup={2}>".format(self.day,self.period,self.studentGroups)

    def isOccupied(self):
        return self._isOccupied
    
    def setOccupied(self,value):
        self._isOccupied = value