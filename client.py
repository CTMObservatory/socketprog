# Echo client program
import socket

HOST = '192.168.2.243'    # The remote host
PORT = 50007              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sa:
    sa.connect((HOST, PORT))
    sa.sendall(b'Hello, world')
    data = sa.recv(1024)
print('Received', repr(data))

