import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=1234
s.bind(("localhost",port))
s.listen(5) 
print ("socket is listening :")
while True:

    # Establish connection with client.
    c, addr = s.accept()
    print ('Got connection from', addr )

    # send a thank you message to the client.
    c.send(b'Thank you for connecting')
    print(c.recv(1024).decode('utf-8'))

    # Close the connection with the client
    c.close()