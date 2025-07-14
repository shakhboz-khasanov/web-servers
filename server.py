import socket
from Constants import SERVER_HOST, SERVER_PORT


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Server_socket:
    Server_socket.bind((SERVER_HOST, SERVER_PORT))
    Server_socket.listen(3)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")
    conn, addr = Server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        with conn:
            print("Waiting for data...")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("No data received, closing connection.")
                    break
                else:
                    print(f"Received: {data.decode()}")
                conn.sendall(data)
