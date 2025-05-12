import socket

host="localhost"
port=1234

client = socket.socket()
client.connect((host,port))
msg=str(input("Type your message: "))

while msg != 'q':
    client.send(msg.encode())
    data=client.recv(1024).decode()
    print("From server: ",data)
    msg=str(input("Type your message: "))
client.close()
