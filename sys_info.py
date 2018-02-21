from __future__ import print_function
import platform
import os
import psutil
pid = os.getpid()
print ("Process ID : ",pid)
py = psutil.Process(pid)
memoryUse = py.memory_info()[0]/2.**30  
print("Memory usage : ", memoryUse)
print ("Processor : ",platform.processor())
per = psutil.cpu_percent()
print ("CPU percent : ",per)
mem = psutil.virtual_memory()
print ("Memory : ",mem)
