import socket
import json


# create a tcp server socket
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind to localhost on port 8080
tcp_server.bind(('localhost', 8080))
tcp_server.listen(5)  # listen for up to 5 connections

print("Server is running on http://localhost:8080")

# accept http requests
while True:
    client_socket, client_address = tcp_server.accept()
    request = client_socket.recv(1024).decode('utf-8')

    if not request:
        client_socket.close()  # close the connection if no request
        continue  # if no request, skip to next iteration

    request_lines = request.splitlines()
    method, path, _ = request_lines[0].split()  # parse request method and path

    print(f"Received {method} request for {path} from {client_address}")

    if path == '/':
        if method == 'GET':
            # handle GET request
            response_body = "Welcome to the HTTP server!"
            response_status = "HTTP/1.1 200 OK"
        elif method == 'POST':
            # handle POST request
            response_body = "POST request received!"
            response_status = "HTTP/1.1 200 OK"
    else:
        # handle other paths
        response_body = "404 Not Found"
        response_status = "HTTP/1.1 404 Not Found"

    client_socket.sendall(f"{response_status}\r\nContent-Type: text/plain\r\nContent-Length: {len(response_body)}\r\n\r\n{response_body}".encode('utf-8'))

    client_socket.close()  # close the client connection

# parse request method and path

# handle GET or POST requests

# return Http response
