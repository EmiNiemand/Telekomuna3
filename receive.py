import encode_decode_message as edm
import send_receive as sr

def main():
    dictionary = edm.create_dictionary()
    encoded_message = sr.receive()
    print(encoded_message)
    decoded_message = edm.decode_message(encoded_message, dictionary)
    print(decoded_message)


if __name__ == '__main__':
    main()