import encode_decode_message as edm
import codecs
import send_receive as sr
import json


def main():
    while True:
        try:
            choice = int(input("'1' - send message, '2' - receive message, '3' - exit program: "))

            if choice == 1:
                with codecs.open('message', 'rb', 'utf-8') as f:
                    message = f.read()
                dictionary = edm.create_dictionary(message)
                encoded_message = edm.encode_message(message, dictionary)
                ip = str(input("Write server IP(IPv4): "))
                port = int(input("Write port number(int > 1000): "))
                sr.send(encoded_message, str(dictionary).encode('utf-8'), ip, port)
                print("Message sent successfully")
            elif choice == 2:
                ip = str(input("Write server IP(IPv4): "))
                port = int(input("Write port number(int > 1000): "))
                encoded_message, dictionary = sr.receive(ip, port)
                dictionary = dictionary.decode('utf-8')
                dictionary = dictionary.replace("'", "\"")
                dictionary = json.loads(dictionary)
                print(encoded_message)
                # f = codecs.open('received_encoded_message.txt', 'w+', 'utf-8')
                # f.write(encoded_message)
                # f.close()
                decoded_message = edm.decode_message(encoded_message.decode('utf-8'), dictionary)
                f = codecs.open('received_message.txt', 'w+', 'utf-8')
                f.write(decoded_message)
                f.close()
                print("Message received successfully")
            elif choice == 3:
                break
            else:
                raise Exception
        except Exception:
            print("Incorrect number")


if __name__ == '__main__':
    main()

