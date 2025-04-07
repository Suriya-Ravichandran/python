import socket

host="192.168.1.6"
port=1234

server=socket.socket()

server.bind((host,port))
server.listen()

conn, addr=server.accept()

while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    data=str(data).capitalize()
    print("From client:"+str(data))
    data=input("Type your message: ")
    conn.send(data.encode())
conn.close()