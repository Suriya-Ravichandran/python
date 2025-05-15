import socket

host="192.168.1.5"
port=1234

server=socket.socket()

server.bind((host,port))
server.listen()
conn,addr=server.accept()

print("Connected by:",addr)

while True:
    incomming=conn.recv(1024).decode()

    if not incomming:
        break
    print("Message From client: ",incomming)
    outgoing=str(input("Type Your message: "))
    conn.send(outgoing.encode())
conn.close()