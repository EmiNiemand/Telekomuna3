from collections import Counter

#klasa pojedynczego węzła drzewa
class NodeTree(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right

    def __str__(self):
        return self.left, self.right


#funkcja znajdująca odpowiednie kodowania w drzewie i zapisująca je do słownika
def huffman_code_tree(node, bin_string=''):
    if type(node) is str:
        return {node: bin_string}
    (l, r) = node.children()
    dictionary = dict()
    dictionary.update(huffman_code_tree(l, bin_string + '0'))
    dictionary.update(huffman_code_tree(r, bin_string + '1'))
    return dictionary


#funkcja tworząca drzewo binarne Huffmana
def make_tree(nodes):
    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = NodeTree(key1, key2)
        nodes.append((node, c1 + c2))
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
    return nodes[0][0]

#wyznaczanie słownika opartego na kodowaniu Huffmana
def encoding(message: str):
    freq = dict(Counter(message))
    #sortowanie znaków od najczęściej występującego do najrzadziej występującego
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    node = make_tree(freq)
    return huffman_code_tree(node)

