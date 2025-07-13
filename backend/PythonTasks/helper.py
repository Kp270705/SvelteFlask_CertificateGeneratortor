from PythonTasks.csvFunc import processFile
from PythonTasks.manageData import processData


def formDataHelper(textData, filePathData):
    # print(f"\nfilePathData: {filePathData}") # it is of dict type.

    # text Data: 
    eventname = textData['eventName']
    orgName = textData['OrgName']
    certType = textData['certificateType']
    certChoice = textData['certificate_choice']
    organizer1_desig = textData['Organizer1Desig']
    organizer2_desig = textData['Organizer2Desig']
    action = textData['action']

    
    # file paths:
    logo1 = filePathData['logo']
    logo2 = filePathData['logo2']
    organizer1_sign = filePathData['organizer1']
    organizer2_sign = filePathData['organizer2']
    csv = filePathData['csv']

    csvData = processFile(csv[0])
    zipPath = processData(csvData, eventname, orgName, certType, organizer1_desig, organizer2_desig, certChoice, action, logo1, logo2, organizer1_sign, organizer2_sign)
    print("\n\n===================================== OUR CONSOLE ENDS HERE ==========================================\n\n\n\n")
    return zipPath

