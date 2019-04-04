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
                # if it is the same stg or the same subject code
                if g.key == v['key'] or g.subjectCode == v['code']:
                    # get venues of student groups
                    for gv in g.venues:
                        # set the venue
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

    def generateTimeTableGreedy(self):
        for sg in self.studentGroups:
            for s in range(len(self.timetable.slots)):
                # if there are no classes
                if len(sg.classes) == 0:
                    continue
                # check same venue
                if sg.venues[0][1][0] == self.timetable.slots[s].venue:
                    duration = sg.classes[0][1]
                    noOfPeriods = int(duration/0.5)

                    # check if it exceeds timetable
                    if(s+noOfPeriods-1 < len(self.timetable.slots)):
                        # check if it is the same day
                        isSameDay = True
                        isOccupied = False
                        checkSgAvail = True
                        isVenue = True
                        currDay = self.timetable.slots[s].day
                        currVenue = sg.venues[0][1][0]
                        for j in range(noOfPeriods-1):
                            day = self.timetable.slots[s+j].day
                            period = self.timetable.slots[s+j].period
                            if currDay != self.timetable.slots[s+j].day:
                                isSameDay = False
                                break
                            if self.timetable.slots[s+j].isOccupied():
                                isOccupied = True
                                break
                            if not sg.checkAvail(day,period):
                                checkSgAvail = False
                                break
                        # if it is the same day and not occupied
                        if isSameDay and not isOccupied and checkSgAvail:
                            for j in range(noOfPeriods-1):
                                self.timetable.slots[s +
                                                     j].studentGroups.append(sg)
                                self.timetable.slots[s+j].setOccupied(True)
                                
                                day = self.timetable.slots[s+j].day
                                period = self.timetable.slots[s+j].period
                                sg.AddTimeSlot(day,period)


                            #remove the class
                            sg.classes.remove(sg.classes[0])


# data structure for student groups
# classes: list of list containing class type and duration
# venues: list of 2 entries [classType,[venues,venues]]
coordinator = Coordinator()
coordinator.generate_timetable()
coordinator.generate_studentGroups()
coordinator.generate_preGroups()
coordinator.assignVenues()
coordinator.add_preGroups()
coordinator.print_studentGroups()
coordinator.generateTimeTableGreedy()
coordinator.print_slots()
