import encode_decode_message as edm
import codecs
import send_receive as sr


def main():
    with codecs.open('message', 'r', 'utf-8') as f:
        lines = f.readlines()
    message = ''
    for line in lines:
        message += str(line)
    dictionary = edm.create_dictionary()
    encoded_message = edm.encode_message(message, dictionary)
    sr.send(encoded_message)


if __name__ == '__main__':
    main()

