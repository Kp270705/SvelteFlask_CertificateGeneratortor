from PythonTasks.csvFunc import processFile
from PythonTasks.genZip import zip_folder
from PythonTasks.getPath import get_Choice_data
from PythonTasks.genPdf import getCertData
from PythonTasks.designTemplate import templatedesign1_2_3, templatedesign4, templatedesign5


def getTemplateContentPath(certificateChoice):
    pathKey = get_Choice_data(certificateChoice)
    return pathKey


def genTemplate(certificateChoice, logo1, logo2, organizer1_sign, organizer2_sign):
    pathKey = getTemplateContentPath(certificateChoice)
    args = [pathKey["TemplatePath"], logo1, logo2, pathKey["linepath"], organizer1_sign, organizer2_sign]
    
    templateDesign = {
        f"Choice1": templatedesign1_2_3,
        f"Choice2": templatedesign1_2_3,
        f"Choice3": templatedesign1_2_3,
        f"Choice4": templatedesign4,
        f"Choice5": templatedesign5,
    }
    templatePath = templateDesign[certificateChoice](args)
    return templatePath

def processData(csvData, eventname, orgName, certType, organizer1_desig, organizer2_desig, certChoice, action, logo1, logo2, organizer1_sign, organizer2_sign):
    template_path = genTemplate(certChoice, logo1, logo2, organizer1_sign, organizer2_sign)
    getCertData(csvData, eventname, orgName, certType, organizer1_desig, organizer2_desig, certChoice, action, template_path)

