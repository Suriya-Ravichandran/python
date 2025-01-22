import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at the specified address and port
client_socket.connect(('localhost', 12345))

# Receive a message from the server
message = client_socket.recv(1024)

# Print the received message
print(f"Message from server: {message.decode()}")

# Close the connection
client_socket.close()
