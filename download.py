import wget
import os
import shutil
#src=os.listdir("home/ec2-user/Python27/python-2.7.14.amd64.msi") #The file actually downloaded
url="http://ftp.jaist.ac.jp/pub/eclipse/oomph/epp/oxygen/R/eclipse-inst-win64.exe"
src=wget.download(url)
print "File Source path is : ",os.path.abspath(src)
des="/home/ec2-user/Downloads" #The file where to keep the downloaded file
#for files in src:
shutil.copy(src,des)  #to copy
print "File Destination pathi is : ",os.path.abspath(des)
#shutil.copy2(src,des)  # to move

