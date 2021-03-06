import huffman_coding as hc

#zwraca słownik stworzony na bazie wiadomości przy użyciu drzewa Huffmana
def create_dictionary(message: str):
    return hc.encoding(message)


#kodowanie wiadomości, zmiana znaku wiadomości na odpowiednik w drzewie
def encode_message(message, dictionary):
    encoded_message = ''
    for word in message:
        encoded_message += dictionary[word]
    return bytes(encoded_message, 'utf-8')

#dekodowanie wiadomości, znajdowanie odpowiednich znaków w słowniku
def decode_message(encoded_message: str, dictionary):
    message = ''
    word = ''
    for i in range(len(encoded_message)):
        word += encoded_message[i]
        try:
            message += find_value_in_dictionary(word, dictionary)
            word = ''
        except Exception:
            pass
    return message


#odnajdowanie znaków na podstawie ciągu 0 i 1
def find_value_in_dictionary(code: str, dictionary):
    for word, dic_code in dictionary.items():
        if dic_code == code:
            return word
    raise Exception
