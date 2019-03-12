from Timetable import Timetable
from StudentGroup import StudentGroup
import InputUtils


class Coordinator:
    def __init__(self):
        self.timetable = -1
        self.preGroups = []
        self.studentGroups = []

    def generate_timetable(self):
        self.timetable = Timetable()
        self.timetable.generate_slots()
        print('Number of slots: {}'.format(len(self.timetable.slots)))

    def generate_studentGroups(self):
        studentGroup = InputUtils.getStudentGroupData()
        for sgd in studentGroup:
            sg = StudentGroup(
                sgd['classKey'],
                sgd['classLabel'],
                sgd['term'],
                sgd['subjectCode'],
                sgd['classSize']
            )
            sg.addClasses(sgd['classes'])
            sg.addVenues(sgd['venues'])
            self.studentGroups.append(sg)

    def generate_preGroups(self):
        blocks = InputUtils.getPreConstraints()
        for b in blocks:
            for s in b['slots']:
                pg = StudentGroup(
                    b['label'],
                    b['label'],
                    0,
                    "00.001",
                    0
                )
                pg.addTimeDateConstraint(
                    b['day'],
                    s,
                    True
                )
                self.preGroups.append(pg)

    def add_preGroups(self):
        for s in self.timetable.slots:
            for p in self.preGroups:
                if s.day == p.day and s.period == p.period:
                    s.studentGroups.append(p)

    def assignVenues(self):
        venues = InputUtils.loadVenues()
        for g in self.studentGroups:
            for v in venues:
                if g.key == v['key'] or g.subjectCode == v['code']:
                    for gv in g.venues:
                        if gv[0] == 'CBL':
                            gv[1] = v['CBLroom']
                        elif gv[0] == 'LEC':
                            gv[1] = v['LECroom']
                        elif gv[0] == 'LAB':
                            gv[1] = v['LABroom']

    def print_studentGroups(self):
        for sg in self.studentGroups:
            sg.print_summary()

    def print_slots(self):
        self.timetable.print_slots()


coordinator = Coordinator()
coordinator.generate_timetable()
coordinator.generate_studentGroups()
coordinator.generate_preGroups()
coordinator.assignVenues()
coordinator.add_preGroups()
coordinator.print_studentGroups()
coordinator.print_slots()
