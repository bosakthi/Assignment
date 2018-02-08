import paramiko
#ssh=paramiko.SSH
##ArithmeticError
def sshCommand(hostname,port,username,password,command):
  sshClient=paramiko.SSHClient() #Creating SSHClient instance
  sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  sshClient.load_system_host_keys()
  sshClient.connect(hostname,port,username,password)
  stdin,stdout,stderr=sshClient.exec_command(command)
  print(stdout.read())

if __name__=='__main__':
    sshCommand('DIN34002216',22,'bosakthi','Akils@007','ls -l')
else:
  print ("something went wrong")

