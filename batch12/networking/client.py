import socket
host = "localhost"
port = 1234
client = socket.socket()
client.connect((host,port))
message = input("type message: ")
while message != 'q':
   client.send(message.encode())
   data = client.recv(1024).decode()
   print ('from server: ' + data)
   message = input("type message: ")
client.close()