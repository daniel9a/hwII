import os
import sys
import socket

port_num = 0
host_list = []
socket_list = []

#loops through global host_list looking for names matching input
#Sends them a kill command, then closes the socket and removes it from the global lists
def sysStop(hostList):
  for i in hostList:
    for j in range(len(host_list)):
      #check if host_list contains host
      if i == host_list[j]:
        print "killing " + host_list[j] + " " + str(j)
        #send kill command to server
        socket_list[j].send("kill")
        #close socket
        socket_list[j].close()
        del socket_list[j]
        del host_list[j]

  #Saves the hostlist to global variable "host_list"
  #also opens sockets for each of the hosts, and stores them in global socket_list
def dInit(hostList): 
  for i in range(0,len(hostList)):
    #This is the best way to copy to avoid the pointer issues with arrays
    host_list.append(hostList[i])
    #Store now opened sockets
    socket_list.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    host = host_list[i]
    #start connection
    socket_list[i].connect((host,port_num))

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
     #This still hangs but at least starts 1 server. Idk how to not make it wait for the server to finish running
     os.system("ssh " + username + "@" + i + " python HwkIIServer.py " + str(port_num))
    """
    command = 'ssh ' + username + '@' + i + ' '
    os.system(command + 'python')
    os.system(command + 'import socket')
    os.system(command + 'import os')
    os.system(command + 's = socket.socket(socket.AF_INET, socket.SOCK_STREAM)')
    os.system(command + 's.bind('', port)')
    """
