import os
import sys
import socket
import thread

#globals
port_num = []
host_list = []


class dFile():
  def __init__(self,fileName):
    self.Name = fileName
    
  def dread(self,size = -1):
    #Use hash to determine which server has filename
    hashNum = hash(self.Name) % len(host_list)

    #open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host_list[hashNum],port_num[0]))

    #send 'read' command
    sock.send('read')

    #Send additional args, like filename and amount of bytes to read.
    sock.send(self.Name + " " + str(size))

    #this could be problematic for large files

    #Default to large size if size isn't included.
    if size < 0:
        size = 1000000
    #Wait to recieve 
    val = sock.recv(size)

    sock.close()

    return val
  
  def dwrite(self,txt):
    return
  
  def dclose():
    #Use hash to determine which server has filename
    hashNum = hash(self.Name) % len(host_list)

    #open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host_list[hashNum],port_num[0]))

    #send 'close' command
    sock.send('clos')
    #send filename to close
    sock.send(self.Name)

    sock.close()
    return

#loops through global host_list looking for names matching input
#Sends them a kill command, then closes the socket and removes it from the global lists
def sysStop(hostList):
  for i in hostList:
    for j in range(len(host_list)):
      #check if host_list contains host
      if i == host_list[j]:
        #open a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host_list[j],port_num[0]))

        sock.send("kill")

        sock.close()
        del host_list[j]

  #Saves the hostlist to global variable "host_list"
  #also opens sockets for each of the hosts, and stores them in global socket_list
def dInit(hostList,port):
  
  #port_num treated like an array to deal with how annoying python scoping is
  port_num.append(port)
  
  for i in range(0,len(hostList)):
    #This is the best way to copy to avoid the pointer issues with arrays
    host_list.append(hostList[i])
    
#return new dFile object, opened
def dOpen(fileName, readWrite):
    #use the hash fn to determine which server has filename
    hashNum = hash(fileName) % len(host_list)

    #open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host_list[hashNum],port_num[0]))

    #Send 'open' command
    sock.send('open')
    #send 'fileName'
    sock.send(fileName + " " + mode)

    sock.close()

    return dFile(fileName)
    
def sysStart(hostList, portNum):
  username = raw_input("Input your username: ")
  threads = []
  for i in hostList:
    t = threading.Thread(target=runSSH(i, portNum, username))
    threads.append(t)
    t.start()
     #This still hangs but at least starts 1 server. Idk how to not make it wait for the server to finish running
def runSSH(i, portNum, userName):     
  os.system("ssh " + username + "@" + i + " python HwkIIServer.py " + str(port_num))
