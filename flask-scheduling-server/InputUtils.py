import pandas as pd
"""Deprecated"""
def readProfCSV():
    df = pd.read_csv("prof.csv",dtype=str)
    return df

def readStgCSV():
    df = pd.read_csv("stg.csv")
    return df

def readRoomCSV():
    df = pd.read_csv("Rooms.csv")
    dict = {}
    for i in df.columns.tolist():
        dict[i] = [i+str(int(x)) for x in df[i].dropna().tolist()]
    return dict

def readCourseCSV():
    df = pd.read_csv("course.csv")
    return df
def inputCSV2df():
    input_df = pd.read_csv('schedule_input.csv')
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
                'term': row['Term'], #3
                'subjectCode': str(round(row['Code'], 3)),#10.009
                'classSize': row['Class Size'],#50
                'classLabel': 'T' + str(row['Term']) + row['Class Labels'] + str(i+1),#T3F1
                'classKey': str(round(row['Code'], 3)) + row['Class Labels'] + str(i+1),#10.009F1
                'classes': [c for c in components if c[0] != 'LEC'],#[['CBL', 1.5], ['CBL', 2.0], ['CBL', 2.0]]
                'venues': [v for v in venues if v[0] != 'LEC']#[['CBL', 'CC'], ['LAB', 'LT']]
            }
            studentGroupData.append(studentGroup)
        if not pd.isnull(row['Common Label']):
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