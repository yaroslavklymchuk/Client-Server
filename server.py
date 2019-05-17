import socket

HOST = 'localhost'
PORT = 9091

def server():
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                print(data)
                if not data:
                    print('Connection Failed')
                    break
                conn.sendall(data)
                
if __name__=='main':
    server()