import socket

host="localhost"
port=1234

server=socket.socket()

server.bind(("192.168.1.8",1234))
server.listen()
conn,adds=server.accept()
print(f"Connected to {adds}")
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    data=str(data)
    print(f"From client: {data}")
    data = input("Type Your message: ")
    conn.send(data.encode())
conn.close()
