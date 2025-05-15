import socket

host="localhost"
port=1234

client=socket.socket()

client.connect((host,port))

outgoing=str(input("Type your message: "))

while outgoing !='q':
    client.send(outgoing.encode())
    incomming=client.recv(1024).decode()
    print("Message from Server:",incomming)
    outgoing=str(input("Type your message: "))
client.close()