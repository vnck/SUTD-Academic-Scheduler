import InputUtils
from Slot import Slot


class Timetable:
    def __init__(self):
        self.days = []
        self.periods = []
        self.slots = []
        self.venues = [] 
        
    def generate_slots(self):
        self.venues = InputUtils.loadVenues()
        venueSet = set()
        for venues in self.venues:
            if venues["CBLroom"]!=None:
                for venueStr in venues["CBLroom"]:
                    venueSet.add(venueStr)
            if venues["LECroom"]!=None:
                for venueStr in venues["LECroom"]:
                    venueSet.add(venueStr)
            if venues["LABroom"]!=None:
                for venueStr in venues["LABroom"]:
                    venueSet.add(venueStr)
        self.days, self.periods = InputUtils.getDaysAndPeriods()
        
        for d in self.days:
            for p in self.periods:
                for venue in venueSet:
                    slot = Slot(d, p,venue)
                    self.slots.append(slot)

    def print_slots(self):
        for i, s in enumerate(self.slots):
            print('slot {}: d: {}, p: {}, , v: {}, sG: {}'.format(
                i, s.day, s.period,s.venue, [g.key for g in s.studentGroups]))
# t = Timetable()
# t.generate_slots()
# t.print_slots()