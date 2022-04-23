import encode_decode_message as edm
import send_receive as sr
import codecs

def main():
    dictionary = edm.create_dictionary()
    encoded_message = sr.receive()
    decoded_message = edm.decode_message(encoded_message, dictionary)
    print(decoded_message)
    f = codecs.open('received_message.txt', 'w+', 'utf-8')
    f.write(decoded_message)
    f.close()

if __name__ == '__main__':
    main()

