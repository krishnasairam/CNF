import socket

def Main():

    HOST = '10.10.9.120'
    PORT = 1087

    rollnumber = input("enter your rollnumber -->")
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(rollnumber.encode())
    temp = s.recv(1024).decode()
    print(temp)
    if (temp != "invalid rollnumber"):
        message = input("enter answer-->")
    else:
        message = "q"
    while  message != 'q':

        try:
            s.send(message.encode())
            data = s.recv(1024)
        except:
            s.close()
            continue
        print("Recieved from server:" + str(data.decode()))
    s.close()

if __name__ == '__main__':
    Main()