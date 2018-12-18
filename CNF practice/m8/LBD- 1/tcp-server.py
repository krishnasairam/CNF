import socket

def Main():

    HOST = '10.10.9.120'
    PORT = 1060

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print ('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode().upper()
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    Main()