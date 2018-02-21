import subprocess


name = input("Enter the Module/Package Name : ")
subprocess.call(['pip', 'install', name])
print("\n##########################\nInstalled Sueecessfully\n##########################")
