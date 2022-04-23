import socket
import time


def send(message):
    # Create a client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect(("172.29.64.1", 2137))
    for byte in message:
        time.sleep(0.05)
        client_socket.send(byte)

def receive():
    # Create a stream based socket(i.e, a TCP socket)
    # operating on IPv4 addressing scheme
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind and listen
    server_socket.bind(("172.29.64.1", 2137))
    server_socket.listen()
    data_from_client = []
    (client_connected, client_address) = server_socket.accept()
    # Accept connections
    while True:
        data = client_connected.recv(16)
        if data:
            data_from_client.append(data)
        else:
            break
    return data_from_client

