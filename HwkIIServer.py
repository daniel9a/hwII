import socket
import os
import sys

#server fn

#sets up the server, making it await incoming calls
#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#take port num as 1st arg to function
port = int(sys.argv[1])

#Associate socket w/ port
host = ''
s.bind((host,port))

#begin waiting for connection
s.listen(1)
(conn, addr) = s.accept()

#once connected keep waiting for client commands until kill command is issued
while(1):
        command = conn.recv(100)

        if command == 'kill':
                s.close()
                exit()
        else:
                print command
