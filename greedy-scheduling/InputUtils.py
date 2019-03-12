import pandas
import numpy as np


def getDaysAndPeriods():
    timetable_df = pandas.read_csv('data/time_data.csv')
    days = timetable_df['days'].dropna().tolist()
    periods = timetable_df['periods'].tolist()
    return days, periods


def inputCSV2df():
    input_df = pandas.read_csv('data/schedule_input.csv')
    return input_df


def getStudentGroupData():
    df = inputCSV2df()
    studentGroupData = []
    for i, row in df.iterrows():
        class_len = row['Classes']
        for i in range(class_len):
            # GET COMPONENTS
            raw_com = row['Components'].split(", ")
            components = [
                [s[:s.find("(")], float(s[s.find("(")+1:s.find(")")])] for s in raw_com]
            # GET VENUES
            raw_ven = row['Room Types'].split(",")
            venues = [s.split(":") for s in raw_ven]
            studentGroup = {
                'term': row['Term'],
                'subjectCode': str(round(row['Code'], 3)),
                'classSize': row['Class Size'],
                'classLabel': 'T' + str(row['Term']) + row['Class Labels'] + str(i+1),
                'classKey': str(round(row['Code'], 3)) + row['Class Labels'] + str(i+1),
                'classes': [c for c in components if c[0] != 'LEC'],
                'venues': [v for v in venues if v[0] != 'LEC']
            }
            studentGroupData.append(studentGroup)
        if not pandas.isnull(row['Common Label']):
            studentGroup = {
                'term': row['Term'],
                'subjectCode': str(round(row['Code'], 3)),
                'classSize': row['Cohort Size'],
                'classLabel': 'T' + str(row['Term']) + row['Common Label'] + '1',
                'classKey': str(round(row['Code'], 3)) + row['Common Label'] + '1',
                'classes': [c for c in components if c[0] == 'LEC'],
                'venues': [v for v in venues if v[0] == 'LEC']
            }
            studentGroupData.append(studentGroup)
    return studentGroupData


def getPreConstraints():
    df = pandas.read_csv('data/schedule_hard_blocks.csv')
    df = df.where(df.notnull(), None)
    hardBlocks = []
    for i, row in df.iterrows():
        slots = [row['startTime'] + i /
                 2 for i in range(int(row['duration'] * 2))]
        hB_dict = {
            'week': row['week'],
            'day': row['day'],
            'slots': slots,
            'label': row['name']
        }
        hardBlocks.append(hB_dict)
    return hardBlocks


def loadVenues():
    df = pandas.read_csv('data/venues.csv')
    df = df.where(df.notnull(), None)
    venues = []
    for i, row in df.iterrows():
        v = {
            'key': row['key'],
            'code': str(round(row['code'], 3)) if row['code'] != None else None,
            'CBLroom': row['CBLroom'].split(",") if row['CBLroom'] != None else None,
            'LECroom': row['LECroom'].split(",") if row['LECroom'] != None else None,
            'LABroom': row['LABroom'].split(",") if row['LABroom'] != None else None
        }
        venues.append(v)
    return venues
