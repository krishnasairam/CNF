from _thread import *
import socket,time
import os
import csv

def Main():
	host = '10.10.9.120'
	port = 1087
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print('Server Started........')
	i = os.getpid()
	print(os.getpid())
	s.listen(10)

	rollnumbers = {}
	attendes = []
	with open ("data.csv", "r") as file:
		reader = csv.reader(file)
		for each in reader:
			rollnumbers[each[0]] = [each[1], each[2]]
	file.close()

	while True:
		c, addr = s.accept()
		rollnumber = c.recv(1024).decode()

		print(rollnumber + " has entered the Server")

		print('Connection Established: ' + str(c) + ':' + str(addr))
		print(start_new_thread( clientthread, (c , rollnumber, rollnumbers)))


def clientthread(conn, rollnumber, rollnumbers):
	y = int(0)

	while True:
		y += 1
		try:
			question = rollnumbers[rollnumber][0]
		except:
			conn.send("invalid rollnumber".encode())
			break;
		conn.send(question.encode())
		data = conn.recv(1024)
		if not data:
			break;
		if data.decode() == 'q':
			print(get_ident())
			return 1

		value = data.decode()
		if (value == rollnumbers[rollnumber][1]):
			conn.send(" ATTENDANCE-SUCCESS ".encode())
			attendes.add(rollnumber)
			conn.close();
			break;
		else:
			conn.send("ATTENDANCE FAILURE ".encode())
			conn.close();
			break;
	conn.close()

if __name__ == '__main__':
	Main()
