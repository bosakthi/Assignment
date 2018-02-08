##For all files in folder

import os, zipfile
folder = 'D:/Users/bosakthi/Downloads/' #Use (/) to specify the path of the folder
extension = ".zip"
os.chdir(folder) # change directory from working dir to dir with files
for item in os.listdir(folder):
    if item.endswith(extension):
        file_name = os.path.abspath(item)
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(folder) # extract file to dir
        zip_ref.close() # close file



##For a particular file
import zipfile
folder = '/home/ec2-user/myzipfile.zip'
zip_ref = zipfile.ZipFile(folder,'r')
zip_ref.extractall('/home/ec2-user/')
zip_ref.close()

#OR

##zip1=zipfile.ZipFile("D:/Users/bosakthi/Downloads/Sakthivel_Boopathi_133479.zip")
##zip1.extractall('D:/Users/bosakthi/Downloads/')
