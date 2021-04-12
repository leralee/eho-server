import socket
from time import sleep


def portVer(port):
    try:
        return True if 1024 <= int(port) <= 65535 else False
    except ValueError:
        return False


def ipVer(ip):
    try:
        sum = 0
        if ip == 'localhost':
            return True
        else:
            parts = ip.split(".")
            # print(len(parts))
            if len(parts) == 4:
                for part in parts:
                    if 0 <= int(part) <= 255:
                        sum += 1
            else:
                return False
            if sum != 4:
                return False
    except ValueError:
        return False


portInput = input("Input port: ")
ipInput = input("Input ip: ")
port_auto = 9090
ip_auto = "127.0.0.1"

if portVer(portInput) is False:
    print(f'You entered incorrect data, default port -  {port_auto}')
    portInput = int(port_auto)
portInput = int(portInput)

if ipVer(ipInput) is False:
    print(f'You entered incorrect data, default ip -  {ip_auto}')
    ipInput = ip_auto
ipInput = str(ipInput)


print(f'Ip -> {ipInput}, port -> {portInput}')
sock = socket.socket()
sock.setblocking(1)
print("~Connection with server~")
sock.connect((ipInput, portInput))

while True:
    message = input("Input message -> ")
    sock.send(message.encode())
    print("Message sended")
    if message == 'exit':
        print(f'We were been disconnected from the server')
        sock.close()
        break
    data = sock.recv(1024)
    print(f'Message get => {data.decode()}')
