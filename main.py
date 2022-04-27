import encode_decode_message as edm
import codecs
import send_receive as sr


def main():
    with codecs.open('message', 'rb', 'utf-8') as f:
        message = f.read()
    dictionary = edm.create_dictionary(message)
    encoded_message = edm.encode_message(message, dictionary)
    sr.send(encoded_message, str(dictionary).encode('utf-8'))


if __name__ == '__main__':
    main()

