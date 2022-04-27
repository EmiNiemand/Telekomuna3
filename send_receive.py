import socket
import time


def send(message):
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect(("127.0.0.1", 2137))
    header = len(message)
    client_socket.send(header.to_bytes(2, "little"))
    client_socket.sendall(message)

def receive():
    # Create a stream based socket(i.e, a TCP socket)
    # operating on IPv4 addressing scheme
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind and listen
    server_socket.bind(("127.0.0.1", 2137))
    server_socket.listen()
    (client_connected, client_address) = server_socket.accept()
    data_length = client_connected.recv(2)
    message = client_connected.recv(int.from_bytes(data_length, "little"))

    return message

