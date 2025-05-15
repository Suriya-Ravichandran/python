import socket

host="192.168.1.5"
port =1234

server=socket.socket()
server.bind((host,port))
server.listen()
conn,addrs=server.accept()
print("Connected by:",addrs)

while True:
    data=conn.recv(1024).decode()
    if not data:
      break
    print("From client:",data)
    msg=str(input("Enter your message: "))
    conn.send(msg.encode())
conn.close()