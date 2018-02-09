import os
import socket
import thread

#globals
port_num = []
host_list = []
thread_list = []
hostTest = ['pc23.cs.ucdavis.edu', 'pc25.cs.ucdavis.edu', 'pc27.cs.ucdavis.edu']

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
    val = ''

    #Default to large size if size isn't included.
    size = 1000
    while True:
      chunk = sock.recv(size)
      if chunk == '':
        break
      else:
        val += chunk             
    sock.close()
    return val
  
  def dwrite(self,txt):
    #Use hash to determine which server has filename
    hashNum = hash(self.Name) % len(host_list)

    #open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host_list[hashNum],port_num[0]))

    #send 'writ' command
    sock.send('writ')

    #Send info to server
    sock.send(self.Name)

    sock.send("{|!|}")

    #send text to server
    sock.send(text)

    sock.close()
  
  def dclose(self):
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
  j = 0

  for i in hostList:
    while j < len(host_list):
      #check if host_list contains host
      if i == host_list[j]:
        #open a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host_list[j],port_num[0]))

        sock.send("kill")

        sock.close()
        del host_list[j]
        
        if not (0 == len(thread_list)):
            del thread_list[j]
        
      else:
        j+=1


  #Saves the hostlist to global variable "host_list"
  #also opens sockets for each of the hosts, and stores them in global socket_list
def dInit(hostList,port):
  
  #port_num treated like an array to deal with how annoying python scoping is
  port_num.append(port)
  
  for i in range(0,len(hostList)):
    #This is the best way to copy to avoid the pointer issues with arrays
    host_list.append(hostList[i])
    
#return new dFile object, opened
def dopen(fileName, mode):
    #use the hash fn to determine which server has filename
    hashNum = hash(fileName) % len(host_list)

    #open a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host_list[hashNum],port_num[0]))

    #Send 'open' command
    sock.send('open')
    #send 'fileName'
    sock.send(fileName + " " + mode)

    key = sock.recv(5000)

    sock.close()

    return dFile(key)
    
def sysStart(hostList, portNum):
  username = raw_input("Input your username: ")
  for i in hostList:
        t = thread.start_new_thread(runSSH,(i, portNum, username))
        #thread_list.append(t) 

def runSSH(i, portNum, userName):     
  os.system("ssh " + userName + "@" + i + " python HwkIIServer.py " + str(portNum))
  thread.exit()
