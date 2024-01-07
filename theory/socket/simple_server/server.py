import socket

HOST = '127.0.0.1'
PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

while True:
    comm_socket, addr_client = server.accept()
    print(f"Connectet to {addr_client}")
    
    # Warning: Only works if there is supposed to be a message
    message = comm_socket.recv(1024).decode()
    print(f"Message {message}")
    comm_socket.send(f"Got your message".encode('utf-8'))
    
    comm_socket.close()
    print(f"Connection with {addr_client} ended!")