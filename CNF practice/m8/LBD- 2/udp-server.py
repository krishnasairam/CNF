import socket

def Main():

    HOST = '10.10.9.120'
    PORT = 1234

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((HOST, PORT))

    print ('server started')
    while True:
        data, addr = s.recvfrom(1024)
        print ('data from ' + str(addr))
        print ('data recieved :' + str(data.decode()) + '\n')
        data = str(data.decode()).upper()
        s.sendto(data.encode(), addr)
    s.close()

if __name__ == '__main__':
    Main()