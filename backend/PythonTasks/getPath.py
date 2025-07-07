CertificateHome = f"./static/Images/Home"
certificate_choice = {
    "Choice1":{
    "TemplatePath" :f"{CertificateHome}/cert_theme1.jpg",
    "logo2Path ": f"{CertificateHome}/TechGeeksLogo.png",

    "auth1Path" : f"{CertificateHome}/auth1White.png",
    "auth2Path" : f"{CertificateHome}/auth2White.png",
    "linepath" : f"{CertificateHome}/line1.png",
    },

    "Choice2":{
    "TemplatePath" :f"{CertificateHome}/cert_theme2.png",
    "logo2Path ": f"{CertificateHome}/TechGeeksLogoColor.png",
    "auth1Path" : f"{CertificateHome}/auth1.png",
    "auth2Path" : f"{CertificateHome}/auth2.png",
    "linepath" : f"{CertificateHome}/line1b.png",
    },
    "Choice3":{
    "TemplatePath" :f"{CertificateHome}/cert_theme3.png",
    "logo2Path ": f"{CertificateHome}/TechGeeksLogoColor.png",
    "auth1Path" : f"{CertificateHome}/auth1.png",
    "auth2Path" : f"{CertificateHome}/auth2.png",
    "linepath" : f"{CertificateHome}/line1b.png",
    },

    "Choice4":{
    "TemplatePath" :f"{CertificateHome}/cert_theme4.png",
    "logo2Path ": f"{CertificateHome}/TechGeeksLogo.png",
    "auth1Path" : f"{CertificateHome}/auth1.png",
    "auth2Path" : f"{CertificateHome}/auth2.png",
    "linepath" : f"{CertificateHome}/line1g.png",
    },


    "Choice5":{
    "TemplatePath" :f"{CertificateHome}/cert_theme5.png",
    "logo2Path ": f"{CertificateHome}/TechGeeksLogoColor.png",
    "auth1Path" : f"{CertificateHome}/auth1.png",
    "auth2Path" : f"{CertificateHome}/auth2.png",
    "linepath" : f"{CertificateHome}/line1g.png",
    },

}

def get_Choice_data(choice):
    return certificate_choice[choice]