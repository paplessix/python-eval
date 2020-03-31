"""
A module that implement the huffman coding algorithm,
with to main class : TreeBuilder that construct the coding tree, 
and Codec that create an object that code and decode text using this tree 

"""

from struct import pack, unpack
import sys


def compt_carac(texte: str):
    """ Function that counts and classifies the different character of a text

    Parameters:
        - texte : the string chain to treat
    Return :
        -  a list of tuple [..., (character, number of occurences), ...] 
            sorted decreasingly
    """
    carac = {}
    for i in texte:
        if i in carac:
            carac[i] += 1
        else:
            carac[i] = 1
    return sorted([(i, carac[i])for i in carac],
                  key=lambda colonnes: colonnes[1], reverse=True)


def index_pos(list: list, weight: int):
    """Returns the index where to insert the leaf in the tree to 
        allow the tree leaves to remain sorted
    """
    i = 0
    while i < len(list)-1 and list[i].weight < weight:
        i += 1
    return i+1


def deci_bin(decimal: int, size=8):
    """Function that return the binary number corresponding to the decimal entered

    It fills it with zeros in order to reach the asked size 
    """
    bin = ''
    if size == 0:  # Cas où le texte encodé est d'une longuer multiple de 8
        return ''
    else:
        while decimal != 0:
            reste = decimal % 2  # permet d'avoir le reste de la division
            bin = str(reste) + bin  # permet de concaténer les deux chaines
            decimal = decimal//2
        while len(bin) < size:  # réajuste la taille de la chaine de caractère
            bin = '0'+bin
        return bin


class Node:
    def __init__(self, NodeL: 'Node', NodeR: 'Node'):
        # a Node is describe with its relation to its children
        self.NodeL = NodeL
        self.NodeR = NodeR
        # a Node weight is the sum of its children's
        self.string = NodeL.string + NodeR.string
        self.weight = NodeL.weight + NodeR.weight


class Leaf:
    def __init__(self, string: str, weight: int):
        self.string = string
        self.weight = weight
        self.NodeL = self  # A leaf has no childrens
        self.NodeR = self  # A leaf has no childrens


class TreeBuilder:
    def __init__(self, text: str):
        self.text = text
        self.caracs = compt_carac(text)

    def tree(self):
        """ module that builds the coding Tree

        Return :
            - a tree is a list of Nodes and Leaves that are bound together 
        """
        tree = []
        for carac, weight in self.caracs:
            tree.append(Leaf(carac, weight))
        tree = sorted(tree, key=lambda value: value.weight)  # keep it sorted
        working_nodes = sorted(tree, key=lambda value: value.weight)
        while len(working_nodes) > 1:
            nodeL = working_nodes.pop(0)
            nodeR = working_nodes.pop(0)
            node = Node(nodeL, nodeR)
            tree.append(node)
            # insert the node at the "right place in" term of sorted weight
            working_nodes.insert(index_pos(working_nodes, node.weight), node)
        return tree


def parcours(racine: Node, walk: str, dic: dict):
    """ Function that creates the translate dictionnary

    Parameters:
        - an existing dictionnary
        - a starting root
        - an empty walk
    Return :
        - None
    """

    if isinstance(racine, Leaf):
        dic[racine.string] = walk
        dic[walk] = racine.string
    else:
        parcours(racine.NodeL, walk + '0', dic)
        parcours(racine.NodeR, walk + '1', dic)


class Codec:

    def __init__(self, binary_tree: list):
        self.binary_tree = binary_tree

    def root_finder(self):
        """Module that returns the top Node of the Tree, needed to know where to start the algorithm
        """
        return max(self.binary_tree, key=lambda x: x.weight)

    root = property(root_finder)

    def dic_builder(self):
        """ Module that builds the translate dic
        """
        dic = {}
        walk = ''
        parcours(self.root, walk, dic)  # lancement construction dictionnaire
        return dic

    dic = property(dic_builder)

    def encode(self, text: str):
        """function that encode according to huffman algorithm
        Parameters
            - str
        Return :
            - str
        """
        encoded = ''
        for letter in text:
            encoded = encoded + self.dic[letter]
        return encoded

    def decode(self, encoded: str):
        """function that decode according to huffman algorithm
        Parameters
            - str
        Return :
            - str
        """
        stock = ""
        decode = ""
        for digit in encoded:
            stock = stock + digit
            # il ne peut y avoir deux Leafs qui ont le même code binaire
            if stock in self.dic:
                decode = decode + self.dic[stock]
                stock = ""
        if stock:
            raise TypeError  # il ne peut y avoir aucune correspondance
        return decode

    def encode_bin(self, text: str):
        """function that encode according to huffman algorithm 
        from string to binary
        """
        Numbers = []
        encoded = self.encode(text)
        for i in range(len(encoded)//8):
            number = int(encoded[i*8:(i+1)*8], base=2)
            Numbers.append(number)
        fin = len(encoded)//8 - 1
        if encoded[(fin+1)*8:] == '':  # cas où on a un multiple de 8
            Numbers.append(0)  # Pour plus de généralité on ajoute deux valeurs
            Numbers.append(0)  # elle seront compris comme '' au décodage
        else:
            number = int(encoded[(fin+1)*8:], base=2)
            # On enregistre la longueurde la dernière découpe pour
            # Pouvoir reconstruire le message
            longueur = len(encoded[(fin+1)*8:])
            Numbers.append(number)
            Numbers.append(longueur)
        encoded_bin = pack('B'*len(Numbers), *Numbers)
        return encoded_bin

    def decode_bin(self, encoded_bin: bytes):
        """function that decode according to huffman algorithm 
        from binary to string
        """
        encoded_deci = unpack('B'*len(encoded_bin), encoded_bin)
        encoded = ''
        for number in encoded_deci[:-2]:
            encoded += f'{deci_bin(number)}'
        encoded += f'{deci_bin(encoded_deci[-2],encoded_deci[-1])}'
        return self.decode(encoded)
