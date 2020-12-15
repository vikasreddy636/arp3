"""
In this program the clint is requested to enter the required letter for moving of the crane
"""
import socket
"""
IPV4 (OR) IPV6 can be selected in the below brackets
"""
c = socket.socket()
"""
IP aaddress of the server must be enterd here and port number can be choosen. Preferred 9999 because of open port
"""
c.connect(('127.0.0.1',9999))
print ("Enter ""A"" to increase by 40\n")
print ("Enter ""B"" to decrease by 40\n")
print ("Enter ""C"" to quit the program\n")
name = input("Enter your requirements\n")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode)
