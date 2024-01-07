import socket
import struct

def start_server():
    server_ip = '192.168.1.58'  # Replace with the actual IP address of the server
    server_port = 12345  # Choose an available port for your server

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        service_id, instance_id, method_id = struct.unpack("!HHH", data)
        
        # Handle the received data as needed for your simulation
        print(f"Received data from {client_address}: ServiceID={service_id}, InstanceID={instance_id}, MethodID={method_id}")

if __name__ == "__main__":
    start_server()
