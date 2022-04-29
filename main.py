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
                sr.send(encoded_message, str(dictionary).encode('utf-8'), ip)
                print("Message sent successfully")
            elif choice == 2:
                ip = str(input("Write server IP(IPv4): "))
                encoded_message, dictionary = sr.receive(ip)
                dictionary = dictionary.decode('utf-8')
                dictionary = dictionary.replace("'", "\"")
                dictionary = json.loads(dictionary)
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

