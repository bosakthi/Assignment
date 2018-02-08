##import os
##import shutil
##os.symlink('Sakthivel_Boopathi_133479.docx', 'resume')
##shutil.move('resume', 'C:/Python27/Assessments/')


import os

src = 'C:\Python27\LICENSE.txt'
dst = 'C:\Users\bosakthi\Desktop'

# This creates a symbolic link on python in tmp directory
os.symlink(src, dst)

print "symlink created"

