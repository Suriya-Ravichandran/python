import socket

host="192.168.1.5"
port =1234

server=socket.socket()

server.bind((host,port))
server.listen()

conn ,addr=server.accept()
print("Connection from: ",str(addr))

while True:
    data=conn.recv(1024).decode()

    if not data:
        break
    data=str(data)
    print("From client: ",data)
    msg=str(input("Type your Messsage: "))
    conn.send(msg.encode())
conn.close()
