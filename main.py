import encode_decode_message as edm
import codecs

def main():
    with codecs.open('message', 'r', 'utf-8') as f:
        lines = f.readlines()
    message = ''
    for line in lines:
        message += str(line)
    dictionary = edm.create_dictionary()
    encoded_message = edm.encode_message(message, dictionary)
    print(encoded_message)
    decoded_message = edm.decode_message(encoded_message, dictionary)
    print(decoded_message)


if __name__ == '__main__':
    main()

