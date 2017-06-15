# Socket Client in Python

import sys
import socket

from settings import settings

try:
    # Create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print('Failed to create socket. Error: {}'.format(e))
    sys.exit()

print('Socket Created')

# Resolve the Hostname

port = settings.port

# Connect to the remote server

s.connect(('', port))

print('Socket Connected to port: {}'.format(port))

# Receive data from server

reply = s.recv(4096)

s.close()

print('Got time from server: {}'.format(reply.decode('utf-8')))