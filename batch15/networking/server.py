import socket

host="localhost"
port=1234

server=socket.socket()
server.bind((host,port))
server.listen()
conn,add=server.accept()

print(f"connection successfully {add}")
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"From client >> {data}")
    msg=str(input("Enter your message: "))
    conn.send(msg.encode())
conn.close()