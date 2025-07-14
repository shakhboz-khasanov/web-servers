import socket
from Constants import SERVER_HOST, SERVER_PORT


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    while True:
        print(f"Connected to server at {SERVER_HOST}:{SERVER_PORT}")

        message = input("Enter message to send (or 'exit' to quit): ")
        print(f"Sending: {message}")
        client_socket.sendall(message.encode())

        response = client_socket.recv(1024)
        print(f"Received: {response.decode()}")
