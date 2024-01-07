import socket

# Configuración del servidor
host = '0.0.0.0'  # Escucha en todas las interfaces de red
port = 12345       # Puerto de escucha

# Función que simula el servicio de la ECU
def simulate_ecu_service(request_data):
    # Aquí puedes procesar la solicitud y devolver una respuesta simulada
    response_data = f"Respuesta de la ECU: {request_data}"
    return response_data

# Creación del socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Enlace y escucha en el puerto
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Servidor ECU simulado escuchando en {host}:{port}")

    # Acepta conexiones entrantes
    connection, client_address = server_socket.accept()

    with connection:
        print(f"Conexión establecida desde {client_address}")

        while True:
            # Recibe datos del cliente
            request_data = connection.recv(1024)

            if not request_data:
                break

            # Simula el servicio de la ECU y envía la respuesta al cliente
            response_data = simulate_ecu_service(request_data.decode())
            connection.sendall(response_data.encode())
