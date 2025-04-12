import socket

client=socket.socket()

host="localhost"
port=1234

client.connect((host,port))
message = str(input("type message: "))
while message != 'q':
   client.send(message.encode())
   data = client.recv(1024).decode()
   print ('Received from server: ' + data)
   message = str(input("type message: "))
client.close()
