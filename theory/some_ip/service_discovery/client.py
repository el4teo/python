import socket
import struct

def discover_service():
    server_ip = '192.168.1.58'  # Replace with the actual IP address of the server
    server_port = 12345  # Replace with the port number used by the server

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    service_id = 1  # Replace with the desired service ID
    instance_id = 1  # Replace with the desired instance ID
    method_id = 1  # Replace with the desired method ID

    data = struct.pack("!HHH", service_id, instance_id, method_id)
    client_socket.sendto(data, (server_ip, server_port))

    print(f"Sent discovery request to {server_ip}:{server_port}")

if __name__ == "__main__":
    discover_service()
