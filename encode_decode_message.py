import huffman_coding as hc
import codecs

def create_dictionary():
    with codecs.open('dictionary', 'r', 'utf-8') as f:
        lines = f.readlines()
    message = ''
    for line in lines:
        message += str(line)
    return hc.encoding(message)


def encode_message(message: str, dictionary):
    encoded_message = []
    for word in message:
        encoded_message.append(bytes(dictionary[word], 'utf-8'))
    return encoded_message


def decode_message(encoded_message: [], dictionary):
    message = ''
    for word in encoded_message:
        message += find_value_in_dictionary(word.decode('utf-8'), dictionary)
    return message


def find_value_in_dictionary(code: str, dictionary):
    for word, dic_code in dictionary.items():
        if dic_code == code:
            return word
    raise Exception
