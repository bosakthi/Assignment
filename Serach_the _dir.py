import os
import re

folder ='/home/ec2-user/dir3/'
directory = 'neds'
result = 'src'
for root, dirs, files in os.walk(folder):
    for name in dirs:
        if name == directory:
             directory = os.path.abspath(os.path.join(root, name))
             for root, dirs, files in os.walk(directory):
                for name in dirs:
                   if name == result:
                      print os.path.abspath(os.path.join(root, name))
