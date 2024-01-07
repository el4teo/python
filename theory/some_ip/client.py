import socket
import struct

# Configuración de la conexión
ip_address = '127.0.0.1'
port = 12345

# Construcción del paquete
message_id = 1234
length = 28  # Longitud del paquete sin contar el encabezado SOME/IP
request_id = 1  # Puede variar según el tipo de mensaje
protocol_version = 1
interface_version = 1
service_id = 0x1234  # Identificador del servicio
method_id = 0x5678  # Identificador del método
client_id = 4321
session_id = 99
data = b'Tus_datos_aqui'

packet = struct.pack('>IIBBHHIHHI', message_id, length, request_id,
                     protocol_version, interface_version, service_id,
                     method_id, client_id, session_id) + data

# Creación del socket y envío del paquete
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(packet, (ip_address, port))