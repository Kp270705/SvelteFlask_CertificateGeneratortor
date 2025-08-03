from PythonTasks.csvFunc import processFile
from PythonTasks.manageData import processData


def formDataHelper(textData, filePathData):
    # print(f"\nfilePathData: {filePathData}") # it is of dict type.

    # text Data: 
    eventname = textData['eventName']
    orgName = textData['organizationName']
    certType = textData['certificateType']
    certChoice = textData['certificate_choice']
    organizer1Desig = textData['organizer1Desig']
    organizer2Desig = textData['organizer2Desig']
    action = textData['action']

    
    # file paths:
    logo1 = filePathData['logo']
    logo2 = filePathData['logo2']
    organizer1Sign = filePathData['organizer1']
    organizer2Sign = filePathData['organizer2']
    csv = filePathData['csv']

    csvData = processFile(csv[0])
    zipPath = processData(csvData, eventname, orgName, certType, organizer1Desig, organizer2Desig, certChoice, action, logo1, logo2, organizer1Sign, organizer2Sign)
    print("\n\n===================================== OUR CONSOLE ENDS HERE ==========================================\n\n\n\n")
    return zipPath

