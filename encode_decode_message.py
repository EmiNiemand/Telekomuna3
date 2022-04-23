def encode_message(message: str, dictionary):
    encoded_message = []
    for word in message:
        encoded_message.append(dictionary[word])
    return encoded_message


def decode_message(encoded_message: str, dictionary):
    message = ''
    for word in encoded_message:
        message += find_value_in_dictionary(word, dictionary)
    return message


def find_value_in_dictionary(code: str, dictionary):
    for word, dic_code in dictionary.items():
        if dic_code == code:
            return word
    raise Exception
