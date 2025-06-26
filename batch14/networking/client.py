import socket

host="192.168.1.8"
port=1234

client=socket.socket()
client.connect((host,port))
msg=str(input("Enter message:"))

while msg !='q':
    client.send(msg.encode())
    data=client.recv(1024).decode()
    print(f"From server: {data}")
    msg=str(input("Enter message:"))
client.close()