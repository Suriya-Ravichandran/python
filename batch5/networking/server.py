import socket

host="192.168.1.6"
port=1234

server=socket.socket()

server.bind((host,port))
server.listen()

conn,add=server.accept()
print ("Connection from: " + str(add))

while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   data = str(data)
   print (" from client: " + str(data))
   data = input("type message: ")
   conn.send(data.encode())

