
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

                fileDict[fileName] = open(fileName,mode)

                conn.close()
                connected = False
