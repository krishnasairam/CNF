import socket

def Main():

    HOST = '10.10.9.120'
    PORT = 1017
    name = input("enter name -->")
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(name.encode())
    print (s.recv(1024).decode())
    message = input("-->")
    while  message != 'q':
        s.send(message.encode())
        data = s.recv(1024)
        print("Recieved from server:" + str(data.decode()))
        message = input("-->")
    conn.close()

if __name__ == '__main__':
    Main()