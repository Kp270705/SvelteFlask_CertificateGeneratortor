
import os, shutil

def checkPDFFolderExist(i):
    if i == 1:
        if os.path.exists("./static/PDFFolder"):
            # print(f"PDFFolder already exists, removing it...")
            shutil.rmtree("./static/PDFFolder")
        os.mkdir("./static/PDFFolder")