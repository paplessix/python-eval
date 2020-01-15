"""
Execute the codec Module, and verify if it's working
"""

from codec import TreeBuilder, Codec
import sys
import matplotlib.pyplot as plt

text = "a dead dad ceded a bad babe a beaded abaca bed"

# on analyse les fréquences d'occurrence dans text
# pour fabriquer un arbre binaire
builder = TreeBuilder(text)
binary_tree = builder.tree()

# on passe l'arbre binaire à un encodeur/décodeur
codec = Codec(binary_tree)
# qui permet d'encoder
encoded = codec.encode_bin(text)
# et de décoder
decoded = codec.decode_bin(encoded)
# si cette assertion est fausse il y a un gros problème avec le code
assert text == decoded

# on affiche le résultat
print(f"{text}\n{encoded}")
if decoded != text:
    print("OOPS")
text = 'ab'
Rang = []
compress_encode = []
compress_huffman = []
compress_binary = []
for rang in range(300):
    texte = text*rang
    taille = sys.getsizeof(texte)
    Rang.append(rang)
    compress_encode.append(taille / sys.getsizeof(codec.encode(texte)))
    compress_huffman.append(taille/sys.getsizeof(codec.encode_bin(texte)))
    compress_binary.append(sys.getsizeof(codec.encode(texte)) /
             sys.getsizeof(codec.encode_bin(texte)))
plt.title('Facteurs de compression')
plt.plot(Rang, compress_encode, label = " facteur de compression par Codec.encode" )
plt.plot(Rang, compress_huffman, label = " facteur de compression de l'algorithme de Huffman")
plt.plot(Rang, compress_binary, label = " facteur de compression d'une str encoded  en binaire ")
plt.legend()

