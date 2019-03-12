import InputUtils
from Slot import Slot


class Timetable:
    def __init__(self):
        self.days = []
        self.periods = []
        self.slots = []

    def generate_slots(self):
        self.days, self.periods = InputUtils.getDaysAndPeriods()
        for d in self.days:
            for p in self.periods:
                slot = Slot(d, p)
                self.slots.append(slot)

    def print_slots(self):
        for i, s in enumerate(self.slots):
            print('slot {}: d: {}, p: {}, sG: {}'.format(
                i, s.day, s.period, [g.key for g in s.studentGroups]))
