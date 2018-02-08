##import os
##import shutil
##os.symlink('Sakthivel_Boopathi_133479.docx', 'resume')
##shutil.move('resume', 'C:/Python27/Assessments/')

#Through Hard Coded Path to create Symbolic links
##import os
##src = 'C:\Python27\LICENSE.txt'
##dst = 'C:\Users\bosakthi\Desktop'
# This creates a symbolic link on python in tmp directory
##os.symlink(src, dst)
##print "symlink created"


import os
# Obtaining the path src file and destination file
src = input('Enter path of file to create symbolic link: ')
dst = input("Enter the destination path of the Symbolic file : ")

# This creates a symbolic link on python in tmp directory
os.symlink(src, dst)

print "symlink created at location : ",dst

