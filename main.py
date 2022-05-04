from sys import *
import clr
clr.AddReference('DLL/ansible_host') # Include Lib
from CSharpAnsible import AnsibleHost # Import C# DLL

AnsibleHost = AnsibleHost('192.168.43.101', 'Artiom', 'azazin')

# OS 
host = ''

# # check os host
# if platform == 'linux' or platform == 'linux2':
#     host = 'linux'
# else:
#     if platform == 'win32':
#         host = 'win32'

# add in ansible file - hosts
# AnsibleHost.WriteOnAnsibleHostFile()

# print all hosts 
#print(AnsibleHost.GetListHosts())

# test info
#print(AnsibleHost.PingHost('Artiom'))

# Print System Info
#print(AnsibleHost.PrintSystemInfo('Artiom'))

# My Command 
print(AnsibleHost.MyCommand('Artiom', 'dir'))