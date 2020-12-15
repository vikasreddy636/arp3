"""
This acts as a server in different machine but shouls be connected to the internet. IPV4 and IPV6 can be entered in the socket. This socket is a bidirectional socket which transfers data from the clint to the server and vice versa
"""
import socket
s = socket.socket()
print('server socket created')
"""
IP numbers should be given to the clint sothat they can connect to this server.If both server and clints are in the same network then th ip address can be replaced by 'local host'
"""
s.bind(('127.0.0.1',9999))
"""
No of clients can be decided here
"""
s.listen(1)
print('waiting')

val=0
"""
Algorithm for the movement of the crane to move forward,backowrds and to stop.
"""
while True:
	c, addr = s.accept()
	name = c.recv(1024).decode()
	inp=name
	if((inp=="A" or inp=="a")):
	print('connected with clint', addr,name)
		if(val<=160):
			val+=40
			print("Value= ",val)
		else:
			print("Maximum limit 200 reached")
	elif((inp=="B" or inp=="b")):
		if(val>=40):
			val-=40
			print("Value= ",val)
		else:
			print("Minimum limit 0 reached")
	elif((inp=="C" or inp=="c")):
		print("Exiting program...")
		exit()
	else:
		print("Invalid command")
	c.send(bytes(('connection secured','utf-8'))
	c.close()
