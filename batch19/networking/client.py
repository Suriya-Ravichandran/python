import socket

host="localhost"
port=1234

client=socket.socket()

client.connect((host,port))
msg=str(input("Enter your message: "))

while msg!="q":
    client.send(msg.encode())
    data=client.recv(1024).decode()
    print(f"from server: {data}")
    msg=str(input("Enter your message: "))
client.close()