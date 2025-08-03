import os
import zipfile

def zip_folder(folder_path, archive_name):
  print(f"\nIn zip folder making")
  with zipfile.ZipFile(archive_name, 'w') as zip_file:
    for root, directories, files in os.walk(folder_path):
      for filename in files:
        file_path = os.path.join(root, filename)
        zip_file.write(file_path, os.path.relpath(file_path, folder_path))

