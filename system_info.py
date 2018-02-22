import os
import platform
import subprocess
import socket

if platform.system() == "Linux":
    command = "cat /proc/cpuinfo"
    all_info = subprocess.check_output(command, shell=True).strip()
    f1 = open("system_info.txt",'w')
    f1.write("CPU Information\n=======================\n")
    f1 = open("system_info.txt",'a')
    f1.write(all_info)
    f1.write("\n----------------------------------------------------------------------------")
    con = socket.gethostbyname(socket.gethostname())
    f1.write("\nHOST NAME : ")
    f1.write(con)
    cmd = "route -n"
    info = subprocess.check_output(cmd, shell=True).strip()
    f1.write("\n---------------------------------\n")
    f1.write(info)
    print "The Informations are Stored in system_info.txt File"
