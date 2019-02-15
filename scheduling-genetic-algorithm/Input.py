import csv
from CourseClass import CourseClass
from Course import Course
from StudentGroup import StudentGroup
from pprint import pprint

raw_courses = []

courses = []
courseClasses = []
studentGroups = []

with open('data/schedule_input.csv', 'r') as f:
    raw_schedule = csv.DictReader(f)
    for row in raw_schedule:
        raw_courses.append(row)


def findStudentGroup(label, code):
    out = []
    for group in studentGroups:
        groupID = group.id.split('-')
        labelID = label.split('-')
        if(groupID[1] == labelID[0] and groupID[0] == code):
            out.append(group)
    return out


for data in raw_courses:

        # Generate Course Objects
    course = Course(
        data['Code'],
        data['Name']
    )
    courses.append(course)

    # Generate StudentGroups
    for groupIdx in range(int(data['Classes'])):
        idxlabel = '0' + \
            str(groupIdx + 1) if groupIdx < 9 else str(groupIdx + 1)
        label = data['Class Labels'] + idxlabel
        studentGroup = StudentGroup(
            data['Code'] + '-' + label,
            label,
            int(data['Class Size']),
            ['']
        )
        studentGroups.append(studentGroup)

    # Generate CourseClass Objects
    for classNum in range(int(data['Classes'])):
        componentStrings = data['Components'].replace(" ", "").split(',')
        components = [comp[:-1].split("(")
                      for comp in componentStrings]

        for i, component in enumerate(components):
            classlabel = '0' + \
                str(classNum+1) if classNum < 9 else str(classNum+1)
            label = data['Class Labels'] + classlabel

            if component[0] in ['LAB', 'LEC']:
                label += '-' + component[0] + str(1)
            else:
                label += '-' + component[0] + str(i+1)

            studentGroup = findStudentGroup(label, data['Code'])

            courseObject = CourseClass(
                data['Code'] + '-' + label,
                label,
                2,
                ['Oka', 'Chris'],
                studentGroup,
                component[1],
                component[0]
            )

            courseClasses.append(courseObject)

for course in courses:
    pprint(vars(course))

for studentGroup in studentGroups:
    pprint(vars(studentGroup))

for classes in courseClasses:
    pprint(vars(classes))
