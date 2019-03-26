class Slot:
    def __init__(self,day,period,room):
        """
        day takes in 1-5
        period takes in float from 8.5 - 17.5
        room takes in a room object
        """
        self.day = day
        self.period = period
        self.room = room
        self.counter = 0
    
    def __repr__(self):
        return "<Slot: day {}  period {}, room {}>".format(self.day,self.period,self.room)

    def getReq(self):
        return self.room.req