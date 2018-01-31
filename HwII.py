import os
import sys
import socket
def sysStop(hostList):
  #Loop through hosts,send each the ssh (?) command to close 

def dInit(hostList):
  global HOST = hostList

def dRead(fileName):
   #Loop through hosts, os.walk to find file, when the file is found open file for reading.    

def dWrite(fileName, writeArg):
  #Loop through hosts, os.walk to find file, when the file is found 

def dClose():

def dOpen(fileName, readWrite):
  for i in HOST:
    #give HOST[i] the SSH command to os.walk, until the file with fileName is 
    #found.
def sysStart(hostList, portNum):
  username = raw_input("Input your username: ")
  for i in hostList:
    command = 'ssh ' + username + '@' + i + ' '
    os.system(command + 'python')
    os.system(command + 'import socket')
    os.system(command + 'import os')
    os.system(command + 's = socket.socket(socket.AF_INET, socket.SOCK_STREAM)')
    os.system(command + 's.bind('', port)')
 
