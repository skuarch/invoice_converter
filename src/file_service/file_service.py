import os
from zipfile import ZipFile

def check_ext(file_path):
    if ".zip" not in file_path:
        print("Error: el programa solo acepta .zip")
        exit()
        
def extract_all(file_path):
    with ZipFile(file_path) as directory:
        directory.extractall("unzip")    
        files = directory.filelist
        return files