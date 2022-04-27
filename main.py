import encode_decode_message as edm
import codecs
import send_receive as sr


def main():
    with codecs.open('message', 'rb', 'utf-8') as f:
        message = f.read()
    dictionary = edm.create_dictionary()
    print(dictionary)
    encoded_message = edm.encode_message(message, dictionary)
    sr.send(encoded_message)


if __name__ == '__main__':
    main()

