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
I=[]
N=[]
B = []
C = []
for rang in range(500):
    texte = text*rang
    taille = sys.getsizeof(texte)
    I.append(rang)
    N.append(taille / sys.getsizeof(codec.encode(texte)))
    B.append(taille/sys.getsizeof(codec.encode_bin(texte)))
    C.append(sys.getsizeof(codec.encode(texte))/sys.getsizeof(codec.encode_bin(texte)))
plt.plot(I,N)
plt.plot(I,B)
plt.plot(I,C)
print(I)