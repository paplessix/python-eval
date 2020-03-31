"""
Execute the codec Module, and verify if it's working
"""

from codec import TreeBuilder, Codec
import sys
import matplotlib.pyplot as plt
def main():
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
    compress_encode = []
    compress_huffman = []
    compress_binary = []

    for rang in range(300):
        
        texte = text*rang # Création d'un texte
        taille = sys.getsizeof(texte) # Espace système de ce texte 
        compress_encode.append(taille / sys.getsizeof(codec.encode(texte)))
        compress_huffman.append(taille/sys.getsizeof(codec.encode_bin(texte)))
        compress_binary.append(sys.getsizeof(codec.encode(texte)) /
                            sys.getsizeof(codec.encode_bin(texte)))
    
    # Affichage
    plt.close()
    plt.title('Facteurs de compression')
    plt.plot( compress_encode, label="Facteur de compression par \n  Codec.encode sortie str")
    plt.plot(compress_huffman,
            label="Facteur de compression de \n l'algorithme de Huffman (Avec Binaire)")
    plt.plot( compress_binary,
            label="Facteur de compression \n d'une str encoded  en binaire ")
    plt.legend()
    plt.show()


def comparaison():
    text = 'Nous sommes en guerre. Aussi, comme je vous l’ai dit jeudi, pour nous protéger et contenir la dissémination du virus, mais aussi préserver nos systèmes de soins, nous avons pris ce matin, entre Européens, une décision commune. Dès demain midi, les frontières à l’entrée de l’Union européenne et de l’espace Schengen seront fermées z w . Concrètement, tous les voyages entre les pays non européens et l’Union européenne seront suspendus pendant trente jours. Les Françaises et les Français qui sont actuellement à l’étranger et souhaitent rentrer pourront bien entendu rejoindre leur pays. Nous devons prendre cette décision parce que je vous demande ce soir d’importants efforts et que nous devons, dans la durée, nous protéger. Et je veux dire à tous nos compatriotes qui vivent à l’étranger que là aussi, en bon ordre, ils doivent se rapprocher des ambassades et consulats et que nous organiserons pour celles et ceux qui le souhaitent, et là où c’est nécessaire, le rapatriement. ? ok '.lower()
    builder = TreeBuilder(text) #Désolé pour le texte en ligne c'est aps très PEP-8 friendly 
    binary_tree = builder.tree()
    codec = Codec(binary_tree)

    texte_french = 'Mes chers compatriotes, alors que je vous parle, les résultats connus nous montrent que vous avez décidé de me confier la plus haute charge de l Etat. J exprime ma profonde gratitude à toutes celles et à tous ceux qui m ont accordé leur confiance et je salue tous les autres avec respect. Mes chers compatriotes, je serai le Président de tous les français'.lower()
    texte_allemand = 'Die Stadt Paris ist fur viele ein Traumziel, das sie wenigstens einmal im Leben besuchen mochten. Wer mochte nicht einmal unter dem Eiffelturm stehen und in den Pariser Himmel hoch schauen? Und dann zu Fuss und mit dem Aufzug wenigstens auf halbe Hohe gelangen und den Blick uber die ganze franzosische Hauptstadt geniessen?'.lower()
    compress_fr,compress_de = [],[]
    for i in range(max( len(texte_french), len(texte_allemand))):
        texte_fr = texte_french[:i] # Création d'un texte
        texte_de = texte_allemand[:i]
        taille_fr = sys.getsizeof(texte_fr) #Espace système de ce texte
        taille_de =  sys.getsizeof(texte_de)
        compress_fr.append(taille_fr/sys.getsizeof(codec.encode_bin(texte_fr)))
        compress_de.append(taille_de/sys.getsizeof(codec.encode_bin(texte_de)))
    plt.close()
    plt.title("Comparaison de l'effet de la langue sur la taux de compression")
    plt.plot( compress_fr, label=" facteur de compression du texte en français ")
    plt.plot( compress_de, label=" facteur de compression du texte en allemand")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
    sys.exit(comparaison())