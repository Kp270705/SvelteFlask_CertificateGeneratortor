import os
import shutil


# How to read, all file names of a folder:
def readFileNames(folderPatha):
    # Get all files and directories
    all_entries = os.listdir(folderPath)
    # Filter only files
    file_names = [f for f in all_entries if os.path.isfile(os.path.join(folderPath, f))]
    print(file_names)


if __name__ == "__main__":
    folderPath = './fonts'
    filesList = readFileNames(folderPath)