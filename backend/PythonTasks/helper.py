from PythonTasks.csvFunc import processFile
from PythonTasks.manageData import processData


def formDataHelper(textData, filePathData):
    # print(f"\nfilePathData: {filePathData}") # it is of dict type.

    '''
    Text data payload:

    textData: {
        'eventName': 'Codethon', 
        'OrgName': 'Gehu', 
        'certificateType': 'of participation', 
        'certificate_choice': 'Choice2', 
        'Organizer1Desig': 'HOD', 
        'Organizer2Desig': 'CC', 
        'action': 'Preview'
    }
    '''
    
    # text Data: 
    eventName = textData['eventName']
    orgName = textData['OrgName']
    certificateType = textData['certificateType']
    certificateChoice = textData['certificate_choice']
    organizer1Desig = textData['Organizer1Desig']
    organizer2Desig = textData['Organizer2Desig']
    action = textData['action']

    # textDataList = [eventname, orgName]



    
    # file paths:
    logo1 = filePathData['logo']
    logo2 = filePathData['logo2']
    organizer1 = filePathData['organizer1']
    organizer2 = filePathData['organizer2']
    csv = filePathData['csv']

    csvData = processFile(csv[0])
    processData(csvData, eventName, orgName, certificateType, organizer1Desig, organizer2Desig, certificateChoice, action, logo1, logo2, organizer1, organizer2)
    print("\n\n===================================== OUR CONSOLE ENDS HERE ==========================================\n\n\n\n")

