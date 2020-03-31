# PYTHON - EVAL

> Evaluation de l ECUE apprentissage de la programmation


***Elève** : Pierre-Adrien PLESSIX P19*

To run this algorithms, please assure you've installed all the requirements listed in `requirements.txt`. If not, run `pip install -r setup.py` in your terminal 

## 1. Algorithme de Needleman-Wunsch
- Algorithme de comparaison de chaînes de protéines. 
- Fonctionne en moins de 3 secondes pour la comparaison de chaînes de 1000 caractères. Attention cela dépend fortement de la machine.
- Pour faire tourner l'agorithme, exécuter `python needleman_wunsch/bundle.py needleman_wunsch/DATASET.txt` ou tout autre fichier test qui vous intéresse.
- Renvoie la comparaison des chaînes inscrites dans `DATASET.txt`
- Renvoie une exception si `Ruler.compute()` n'est pas lancé avant d'accéder à l'attribut `distance`.

## 2. Codage de Huffman
- Algorithme de compression du langage.
- Executer `python huffman/exec.py`
- Prend en charge le codage en bits réels de la compression.
- Renvoie le texte initiale codé en `bytes`, ainsi que la vérification de la fidélité de l'opération codage / décodage.
-  Renvoie des graphiques de **comparaison du facteur de compression** des différentes opérations de compression.
-  Renvoie une comparaison de l'efficacité du codage en fonction de **la langue utilisée**.

**Bon confinement !**