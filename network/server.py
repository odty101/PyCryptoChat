import sys
import socket
import time

from settings import settings


try:
    # Create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print('Failed to create socket. Error: {}'.format(e))
    sys.exit()

port = settings.port

try:
    # Bind to the port
    s.bind(('', port))
except socket.error:
    print('Unable to bind to port: {}'.format(port))
    sys.exit()
print('Bound to port: {}'.format(port))

# Queue up to 5 requests
s.listen(5)

while True:
    # Establish a connection
    client_socket, addr = s.accept()

    print('Got connection from {}'.format(str(addr)))

    # Send current time to client
    current_time = time.ctime(time.time()) + '\r\n'
    client_socket.send(current_time.encode('utf-8'))
    client_socket.close()