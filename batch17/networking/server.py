import socket

host="192.168.1.11"
port=1234


server=socket.socket()
server.bind((host,port))
server.listen()

conn,adds=server.accept()
print(f"connected by :{adds}")

while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    print(f"From client: {data}")
    msg=str(input("Enter your message: "))
    conn.send(msg.encode())
conn.close()