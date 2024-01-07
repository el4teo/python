~~~ txt
                                   
  ______ ____ _____  ______ ___ __ 
 /  ___// ___\\__  \ \____ <   |  |
 \___ \\  \___ / __ \|  |_> >___  |
/____  >\___  >____  /   __// ____|
     \/     \/     \/|__|   \/     
~~~

[BACK](../THEORY.md)

- [Resources](#resources)
- [Theory](#theory)
  - [Features](#features)
  - [Instalation and Requirements](#instalation-and-requirements)
  - [Tutorial](#tutorial)
- [Practice](#practice)

# Resources

[web](https://scapy.net/)
[docs](https://scapy.readthedocs.io/en/latest/)
[repo](https://github.com/secdev/scapy)

[David Bombal](https://github.com/davidbombal/scapy)

# Theory

## Features

- Is a powerful interactive packet manipulation library written in Python.
- Forge or decode packets of a wide number of protocols
- Some of its capabilities:
  - Send them on the wire
  - Capture them
  - Match requests and replies
- Can be used as a REPL (Read-Eval-Print-Loop) or as a library.
- Provides all the tools and documentation to quickly add custom network layers.
- Runs natively on Linux, macOS, most Unixes.
- Runs on Windows with Npcap.

## Instalation and Requirements

- With pip:
  - `pip install scapy`

- From github:

~~~ sh
git clone --depth 1 https://github.com/secdev/scapy
cd scapy
# Start REPL (Read-Eval-Print-Loop)
sudo ./run_scapy
~~~

- It must be run with admin permissions

## Tutorial

[Scapy in 30 minutes](./Scapy%20in%200x30%20minutes.ipynb)

- [Online](https://github.com/guedou/guedou.github.io/blob/master/talks/2022_GreHack/Scapy%20in%200x30%20minutes.ipynb)
- [Slides](https://guedou.github.io/talks/2022_GreHack/Scapy%20in%200x30%20minutes.slides.html#/)

Content:

- Packets manipulation
- Interacting with the network
- Visualization
- Using Scapy as a Python module
- Implementing a new protocol
- Answering machines
- IPv6 reconnaissance
- X.509 certificates manipulation
- TLS tricks
- Advanced features: automaton, pipes


# Practice
