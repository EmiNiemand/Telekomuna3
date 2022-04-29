import socket
import time


def send(message, dictionary, ip: str):
    for i in range(10):
        time.sleep(1)
        try:
            # tworzenie socketu klienta
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # łączenie się z serverem
            client_socket.connect((ip, 2137))
            dictionary_length = len(dictionary)
            #przesłanie długości słownika i samego słownika
            client_socket.send(dictionary_length.to_bytes(2, "little"))
            client_socket.sendall(dictionary)
            data_length = len(message)
            # przesłanie długości wiadomości i samej wiadomości
            client_socket.send(data_length.to_bytes(2, "little"))
            client_socket.sendall(message)
            break
        except Exception:
            pass

def receive(ip: str):
    # Tworzenie socketu TCP
    # operującego na adresie IPv4
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Powiązanie adresu ip z socketem i rozpoczęcie nasłuchiwania
    server_socket.bind(("127.0.0.1", 2137))
    server_socket.listen()
    #zaakceptowanie połączenia od klienta
    (client_connected, client_address) = server_socket.accept()
    # odebranie długości słownika i samego słownika
    dictionary_length = client_connected.recv(2)
    dictionary = client_connected.recv(int.from_bytes(dictionary_length, "little"))
    # odebranie długości wiadomości i samej wiadomości
    data_length = client_connected.recv(2)
    message = client_connected.recv(int.from_bytes(data_length, "little"))

    return message, dictionary

