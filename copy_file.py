import os
filePath = "/home/ec2-user/system_info.txt"
serverPath = "/home/ec2-user/a1/syst.txt"
os.system("scp "+filePath+" ec2-18-218-23-174.us-east-2.compute.amazonaws.com:"+serverPath)
print "File Copied Successfully"
