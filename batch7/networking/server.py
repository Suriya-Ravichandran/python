import socket

server=socket.socket()

host="192.168.1.6"
port=1234

server.bind((host,port))
server.listen()
conn,addr=server.accept()
print("connetion from: ",str(addr))

while True:
   data = conn.recv(1024).decode()
   if not data:
      break
   data = str(data)
   print ("from client: " + str(data))
   data = str(input("type message: "))
   conn.send(data.encode())
conn.close()