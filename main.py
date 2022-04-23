import huffman_coding as hc
import encode_decode_message as edm

def main():
    with open('message') as f:
        lines = f.readlines()
    message = ''
    for line in lines:
        message += str(line)
    dictionary = hc.encoding(message)
    encoded_message = edm.encode_message(message, dictionary)
    print(encoded_message)
    decoded_message = edm.decode_message(encoded_message, dictionary)
    print(decoded_message)


if __name__ == '__main__':
    main()

