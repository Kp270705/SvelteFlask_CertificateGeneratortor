# data validation creating objects of each row of csv file:- 

import csv

class Participants:
    def __init__(self, name, course, sId, emailId, semester, date):
        self.name = name
        self.course = course
        self.sId = sId
        self.emailId = emailId
        self.semester = semester
        self.date = date 

# main logic of code: 
def processFile(csv_file_path):
    Local_workout_data = []

    with open(csv_file_path, 'r') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            name = str(row["Name"]) if row["Name"] else " "
            course = str(row["Course"]) if row["Course"] else " "
            sId = str(row["ID"]) if row["ID"] else " "
            emailId = str(row["email"]) if row["email"] else " "
            semester = str(row["Semester"]) if row["Semester"] else " "
            date = str(row["Date"]) if row["Date"] else " "


            workout_obj= Participants(name, course, sId, emailId, semester, date)
            Local_workout_data.append(workout_obj)
            
    return(Local_workout_data)