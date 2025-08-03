certTemplates =     f"./static/Images/certTemplates"
userSubmitLogo =    f"./static/Images/userSubmitData/logos"
userSubmitAuth =    f"./static/Images/userSubmitData/authoritySigns"
underLines =        f"./static/Images/underLines"

certificate_choice = {
    "Choice1":{
    "TemplatePath" :f"{certTemplates}/certTemplate1.jpg",
    "logo2Path": f"{userSubmitLogo}/TechGeeksLogo.png",

    "auth1Path" : f"{userSubmitAuth}/auth1White.png",
    "auth2Path" : f"{userSubmitAuth}/auth2White.png",
    "linepath" : f"{underLines}/lineW.png",
    },

    "Choice2":{
    "TemplatePath" :f"{certTemplates}/certTemplate2.png",
    "logo2Path": f"{userSubmitLogo}/TechGeeksLogoColor.png",
    "auth1Path" : f"{userSubmitAuth}/auth1.png",
    "auth2Path" : f"{userSubmitAuth}/auth2.png",
    "linepath" : f"{underLines}/lineB.png",
    },
    "Choice3":{
    "TemplatePath" :f"{certTemplates}/certTemplate3.png",
    "logo2Path": f"{userSubmitLogo}/TechGeeksLogoColor.png",
    "auth1Path" : f"{userSubmitAuth}/auth1.png",
    "auth2Path" : f"{userSubmitAuth}/auth2.png",
    "linepath" : f"{underLines}/lineB.png",
    },

    "Choice4":{
    "TemplatePath" :f"{certTemplates}/certTemplate4.png",
    "logo2Path": f"{userSubmitLogo}/TechGeeksLogo.png",
    "auth1Path" : f"{userSubmitAuth}/auth1.png",
    "auth2Path" : f"{userSubmitAuth}/auth2.png",
    "linepath" : f"{underLines}/lineG.png",
    },


    "Choice5":{
    "TemplatePath" :f"{certTemplates}/certTemplate5.png",
    "logo2Path ": f"{userSubmitLogo}/TechGeeksLogoColor.png",
    "auth1Path" : f"{userSubmitAuth}/auth1.png",
    "auth2Path" : f"{userSubmitAuth}/auth2.png",
    "linepath" : f"{underLines}/lineG.png",
    },

}

def get_Choice_data(choice):
    return certificate_choice[choice]
