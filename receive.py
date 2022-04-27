import encode_decode_message as edm
import send_receive as sr
import codecs
import json

def main():
    encoded_message, dictionary = sr.receive()
    dictionary = dictionary.decode('utf-8')
    dictionary = dictionary.replace("'", "\"")
    dictionary = json.loads(dictionary)
    decoded_message = edm.decode_message(encoded_message.decode('utf-8'), dictionary)
    f = codecs.open('received_message.txt', 'w+', 'utf-8')
    f.write(decoded_message)
    f.close()

if __name__ == '__main__':
    main()

