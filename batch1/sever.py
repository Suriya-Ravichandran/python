import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port
server_socket.bind(('localhost', 12345))

# Enable the server to listen for connections
server_socket.listen(1)

print("Server is listening on port 12345...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Send a message to the client
client_socket.send(b"Hello from the server!")

# Close the connection
client_socket.close()
server_socket.close()
