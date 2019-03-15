# -*- coding: utf-8 -*-
from ortools.sat.python import cp_model
num_of_days = 5
# 8:30 to 18:00 30 minute periods
num_of_periods = 20
num_of_rooms = 30
num_of_student_groups = 30
num_of_courses = 30
num_of_instructors = ["gary", "john", "may", "jean", "jack"]
num_of_room_req = 3  # lab,lec,cbl

model = cp_model.CpModel()

courseclass = {}

for day in range(num_of_days):
    for period in range(num_of_periods):
        for room in range(num_of_rooms):
            for stg in range(num_of_student_groups):
                for course in range(num_of_courses):
                    for instructor in num_of_instructors:
                        for roomReq in range(num_of_room_req):
                            courseclass[(day, period, room, stg, course, instructor, roomReq)] = \
                                model.NewBoolVar("{}{}{}{}{}{}{}".format(
                                    day, period, room, stg, course, instructor, roomReq))

# Ensures that each course is taught
for course in range(num_of_courses):
    model.Add(sum(courseclass[(day, period, room, stg, course, instructor, roomReq)] for day in range(num_of_days)
                  for period in range(num_of_periods)
                  for room in range(num_of_rooms)
                  for stg in range(num_of_student_groups)
                  for instructor in num_of_instructors
                  for roomReq in range(num_of_room_req)
                  ) == 1)

# Ensures that for each day each period each room, the sum of the courses/student groups/instructor/room req is 1
#i.e cannot have more than 1 instructor/course/student group/room req at any point in time
for day in range(num_of_days):
    for period in range(num_of_periods):
        for room in range(num_of_rooms):
            model.Add(sum(courseclass[(day, period, room, stg, course, instructor, roomReq)]
                          for course in range(num_of_courses)
                          for stg in range(num_of_student_groups)
                          for instructor in num_of_instructors
                          for roomReq in range(num_of_room_req)
                          ) <= 1)

print("solving")
solver = cp_model.CpSolver()
solver.Solve(model)
print("solved")


for day in range(num_of_days):
    print("Day ", day)
    for period in range(num_of_periods):
        for room in range(num_of_rooms):
            for stg in range(num_of_student_groups):
                for course in range(num_of_courses):
                    for instructor in num_of_instructors:
                        for roomReq in range(num_of_room_req):
                            if solver.Value(courseclass[(day, period, room, stg, course, instructor, roomReq)]) == 1:
                                print(
                                    "period {},room {},stg {},course {},instructor {},roomReq {}".format(period, room, stg, course, instructor, roomReq))
