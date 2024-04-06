
from socket import *

# Set the server IP address and port number
server_ip = "192.168.1.166"  # Listen on all available network interfaces
server_port = 12000  # Choose a port number (e.g., 12345)

# Create a server socket
server_socket = socket(AF_INET, SOCK_STREAM)

# Bind the server socket to the address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)
print("The server is ready to recieve...")

while True:
    # Accept an incoming connection
    client_socket, client_address = server_socket.accept()
    # Receive data from the client
    received_data = client_socket.recv(2048)
    print("\nHTTP request:")
    print(f"GET /{received_data.decode()} HTTP/1.1")
    print(f"Host: {server_ip}")

    print(f"\nObject to be fetched: {received_data.decode()}")

    try:
        # if file requested file is in the directory then will complete the following
        with open(received_data.decode(), 'r') as file: 
            file_content = file.read()
            print("Object content:")
            print(file_content)
            response_message = "HTTP/1.1 200 OK"
            # will first send the HTTP 200 response followed by the contents of the file
            client_socket.send(response_message.encode())
            client_socket.send(file_content.encode())
            print("\nHTTP response message:")
            print(response_message)
            print("")
            print(file_content)
    # if the file is not in the directory then the following actions are completed
    except FileNotFoundError:
        print("HTTP response message:")
        # HTTP 404 response is sent to the client along with an empty string
        response_message = "HTTP/1.1 404 Not Found"
        file_content = ""
        client_socket.send(response_message.encode())
        # client_socket.send(file_content.encode())
        print(response_message)

    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()