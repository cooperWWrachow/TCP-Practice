
from socket import *
import sys

# A message is displayed if argument count is not correct 
if len(sys.argv) != 4:
        print("Usage: python TCPClient.py <server_ip> <server_port> <filename>")
        quit()

# the arguments are parsed and assigned to correct variables
server_ip = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3] 

# Create a TCP socket and connect to the server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_ip, server_port))
print("HTTP request to server:")
print(f"GET /{filename} HTTP/1.1")
print(f"Host: {server_ip}")
print("\nHTTP response from server:")

client_socket.send(filename.encode())

# the server's response/responses are displayed then the socket is closed 
response = client_socket.recv(1024).decode()
print(response)
content = client_socket.recv(1024).decode()
print("")
print(content)
print("")

client_socket.close()