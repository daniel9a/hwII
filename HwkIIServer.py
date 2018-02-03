
import socket
import os
import sys

fileDict = {}
connected = False

#server fn

#sets up the server, making it await incoming calls
#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#take port num as 1st arg to function
port = int(sys.argv[1])

#Associate socket w/ port
host = ''
s.bind((host,port))

while(1):

        if connected == False:
                #wait for a connection
                s.listen(1)
                (conn, addr) = s.accept()
                connected = True

        #Get the command from the client
        command = conn.recv(4)

        #If the command is 'kill' end the server
        if command == 'kill':
                s.close()
                exit()

        #open a file on the server
        elif command == 'open':
                [fileName, mode] = conn.recv(5000).split(" ")

                print "opening " + fileName + " " + mode

                fileStore = fileName + str(addr[0]) + str(addr[1])

                fileDict[fileStore] = open(fileName,mode)

                conn.send(fileStore)

                conn.close()
                connected = False

        #Close the file and remove it from the file list                
        elif command == "clos":
                fileName = conn.recv(5000)

                print "closing " + fileName

                fileDict[fileName].close()
                del fileDict[fileName]

                conn.close()
                connected = False

        #read a file and send output to client
        elif command == "read":
                incoming = conn.recv(5000)

                print incoming

                [fileName, size] = incoming.split(" ")

                print "reading " + fileName + " " + size

                x = fileDict[fileName].read(int(size))

                conn.send(x)

                conn.close()
                connected = False

                
        #need to change this to allow for writes large than 5000000 bytes
        elif command == "writ":
                while True:
                        chunk = conn.recv(5000)
                        if chunk == '':
                                break
                        else:
                                incoming += chunk

                print incoming
                
                [fileName,data] = incoming.split("{|!|}")

                fileDict[fileName].write(data)

                conn.close()
                connected = False

