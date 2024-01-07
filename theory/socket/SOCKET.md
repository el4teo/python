~~~ txt
                     __           __   
  __________   ____ |  | __ _____/  |_ 
 /  ___/  _ \_/ ___\|  |/ // __ \   __\
 \___ (  /_\ )  \___|    <\  ___/|  |  
/____  >____/ \___  >__|_ \\___  >__|  
     \/           \/     \/    \/      
~~~

[BACK](../THEORY.md)

- Simple server
  - [client.py](./simple_server/client.py)
  - [server.py](./simple_server/server.py)

**CONTENT**

- [Resources](#resources)
- [Fundamentals - NeuralNine](#fundamentals---neuralnine)
  - [OSI Layers](#osi-layers)
  - [Client-server architecture](#client-server-architecture)
  - [IP addresses](#ip-addresses)
  - [Sockets](#sockets)
    - [When mounting a server](#when-mounting-a-server)
    - [TCP](#tcp)
    - [UDP](#udp)
- [REST](#rest)


# Resources

[library](https://docs.python.org/3/library/socket.html)

# Fundamentals - NeuralNine

Basic concepts

- Client
- Server
- Client-Server architecture
- Router
- LAN (Local Area Network)
- Local IP address
- Public IP address
- Ports
- Socket
- Protocols
  - TCP
  - UDP
- Basics of [OSI model](https://es.wikipedia.org/wiki/Modelo_OSI)

## OSI Layers

![PDUs](https://upload.wikimedia.org/wikipedia/commons/f/fc/PDUs.PNG)

| No. | Layer        | Protocol data unit (PDU) |
|-----|--------------|--------------------------|
| 7   | Application  | Data                     |
| 6   | Presentation | Data                     |
| 5   | Session      | Data                     |
| 4   | Transport    | Segment, Datagram        |
| 3   | Network      | Packet                   |
| 2   | Data link    | Frame                    |
| 1   | Physical     | Bit, Symbol              |

- Host layers = [7, 6, 5, 4]
- Media layers = [3, 2, 1]

1. Physical: Transmission and reception of raw bit streams over a physical medium.
2. Data: Transmission of data frames between two nodes connected by a physical layer.
3. Session: Structuring and managing a multi-node network, including addressing, routing and traffic control.
4. Network: Reliable transmission of data segments between points on a network, including segmentation, acknowledgement and multiplexing.
5. Transport: Managing communication sessions, i.e., continuous exchange of information in the form of multiple back-and-forth transmissions between two nodes.
6. Presentation: Translation of data between a networking service and an application; including character encoding, data compression and encryption/decryption.
7. Application: High-level protocols such as for resource sharing or remote file access, e.g. HTTP.

## Client-server architecture

- A way to structure the idea with clients and resrvers
- The messages pass always though the server (not P2P)
- Examples:
  - Chat room
  - Gamming cross-platform server

## IP addresses 

## Sockets

- It is a communication end point
- `AF_INET`: Internet socket IPV4
- `AF_INET6`: Internet socket IPV6
- It doesn't need to be connected to internet
  - Bluetooth sockets
  - Internal applications sockets
  - OS level sockets
  - Infrared sockets
- Different internet sockets
  - `SOCK_STREAM`: For `TCP`
  - `SOCK_DGRAM`: For `UDP` 
  - When the socket type is choosen, python socket lib chooses the protocol automatically

### When mounting a server

- We get a new socket for each connection that is accepted

### TCP

- TCP (Transmisions Control Protocol)
- Connection-based
  - One point to another
- Relaiable
  - You have confirmations
- Sequential
- Byte stream
- Keeps up Connection

### UDP

- UDP (Datagram User Protocol) 
- Not relaiable
- Not sequential (no order)
- Fast!!
- Less network and PC stress

# REST

[realpython](https://realpython.com/api-integration-in-python/)

IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
<IP frag=0 proto=TCP |<TCP |<Raw load='GET / HTTP/1.0\r\n\r\n' |>>>

