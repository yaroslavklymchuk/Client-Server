import socket


HOST = 'localhost'
PORT = 9091


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

        print('Received', repr(data))



if __name__=='main':
    client()