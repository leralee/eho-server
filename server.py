import errno
import socket


def clean():
    file = open("logFile.txt", 'w+')
    file.seek(0)
    file.close()


def writeData(data):
    with open("logFile.txt", "a") as file:
        file.write(f'{data}\n')


def freePort(sock, s_port):
    try:
        sock.bind(('', s_port))
        print(f'Port: {s_port}')
        return True
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            s_port += 1
            return freePort(sock, s_port)


clean()
sock = socket.socket()
s_port = 9090


if freePort(sock, s_port):
    print("Start listening on a port")
    writeData("Start listening on a port")
    sock.listen(1)

    while True:
        file = open('logFile.txt', 'a')
        conn, addr = sock.accept()
        running = True
        print(f'Client {addr} was connected')
        writeData(f'Client {addr} was connected\n')
        while running:
            data = conn.recv(1024)
            if not data:
                print(f'Client {addr} was disconnected')
                writeData(f'Client {addr} was disconnected\n')
                break
            if data.decode() == 'exit':
                print('Server stoped')
                writeData('Server stopped\n')
                running = False
                break
            print(f'Get message{data.decode()}')
            print(f'Sent message: {data.decode()}')
            writeData(f'Get message::{data.decode()}')
            writeData(f'Sent message:: {data.decode()}')
            conn.send(data)