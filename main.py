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
                encoded_message = encoded_message.decode('ascii')
                new_message = bytes()
                for j in range(0, int(len(encoded_message)), 8):
                    byte = ''
                    for k in range(8):
                        if k+1+j > len(encoded_message):
                            break
                        byte += encoded_message[j + k]
                    helper = int(byte, 2).to_bytes(1, byteorder='big')
                    new_message += helper
                ip = str(input("Write server IP(IPv4): "))
                port = int(input("Write port number(int > 1000): "))
                sr.send(new_message, str(dictionary).encode('utf-8'), ip, port)
                print("Message sent successfully")
            elif choice == 2:
                ip = str(input("Write server IP(IPv4): "))
                port = int(input("Write port number(int > 1000): "))
                encoded_message, dictionary = sr.receive(ip, port)
                dictionary = dictionary.decode('utf-8')
                dictionary = dictionary.replace("'", "\"")
                dictionary = json.loads(dictionary)
                decoded_message = edm.decode_message(encoded_message, dictionary)
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

