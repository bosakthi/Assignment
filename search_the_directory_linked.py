import os
import re

folder ='/'
directory = 'neds'
result = 'src'
for root, dirs, files in os.walk(folder):
    for name in dirs:
        if name == directory:
             directories = os.path.abspath(os.path.join(root, name))
             for root, dirs, files in os.walk(directories):
               for name in dirs:
                   if name == result:
                      print os.path.abspath(os.path.join(root, name))
                    
