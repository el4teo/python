import socket

HOST = '127.0.0.1'
PORT = 9999

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.connect((HOST, PORT))

socket_server.send("Hello Atria!".encode('utf-8'))
print(socket_server.recv(1024).decode())