import os
import re
import glob

src = 'src.txt' #specify the file name
path = '/user/ec2-user/'#specify the server path
for infile in glob.glob( os.path.join(path, '*') ):
    if src.match(infile):
         print "current file is: " + infile
