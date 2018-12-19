import socket

def Main():

    HOST = '10.10.9.120'
    PORT = 1235
    server = ('10.10.9.120', 1234)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))

    message = input("-->")

    while  message != 'q':
        s.sendto(message.encode(), server)
        data, addr = s.recvfrom(1024)
        print("Recieved from server:" + str(data.decode()) + '\n')
        message = input("-->")
    s.close()

if __name__ == '__main__':
    Main()