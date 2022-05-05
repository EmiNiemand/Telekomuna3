import socket
import time

#funkcja odpowiedzialna za wysłanie wiadomości
def send(message, dictionary, ip: str, port: int):
    for i in range(10):
        time.sleep(1)
        try:
            # tworzenie socketu klienta
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # łączenie się z serverem
            client_socket.connect((ip, port))
            dictionary_length = len(dictionary)
            #przesłanie długości słownika i samego słownika
            client_socket.send(dictionary_length.to_bytes(2, "little"))
            client_socket.sendall(dictionary)
            # przesłanie długości wiadomości i samej wiadomości
            data_length = len(message)
            client_socket.send(data_length.to_bytes(2, "little"))
            client_socket.sendall(message)
            break
        except Exception:
            pass


#funckja odpowiedzialna za odebranie wiadomości
def receive(ip: str, port: int):
    # Tworzenie socketu TCP
    # operującego na adresie IPv4
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Powiązanie adresu ip z socketem i rozpoczęcie nasłuchiwania
    server_socket.bind((ip, port))
    server_socket.listen()
    #zaakceptowanie połączenia od klienta
    (client_connected, client_address) = server_socket.accept()
    # odebranie długości słownika i samego słownika
    dictionary_length = client_connected.recv(2)
    dictionary = client_connected.recv(int.from_bytes(dictionary_length, "little"))
    # odebranie długości wiadomości i samej wiadomości
    data_length = client_connected.recv(2)
    message = client_connected.recv(int.from_bytes(data_length, "little"))
    # f = open('received_encoded_message.txt', 'wb+')
    # f.write(message)
    # f.close()
    new_message = ''
    for byte in message:
        new_message += f'{int(byte):08b}'
    new_message = new_message[:-7]
    new_message += bin(int(message[-1]))[2:]
    return new_message, dictionary

