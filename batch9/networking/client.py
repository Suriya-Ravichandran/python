import socket

host="localhost"
port=1234

client=socket.socket()

client.connect((host,port))

message = input("Enter your message: ")
while message != 'q':
    client.send(message.encode())
    data=client.recv(1024).decode()
    print("From server:",data)
    message = input("Enter your message: ")
client.close()