import socket

host="localhost"
port=1234

client=socket.socket()

client.connect((host,port))
message = input("Type your message: ")
while message != 'q':
   client.send(message.encode())
   data = client.recv(1024).decode()
   print(f"From server: {data}")
   message = input("Type your message: ")
client.close()