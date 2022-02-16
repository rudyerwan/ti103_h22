# Copyright 2022 Guillaume Mantelet - All rights reserved. Niark

#
# 1. Commentaires
#
# Pour écrire un commentaire, on démarre une ligne avec '#'
#
# Un commentaire n'est JAMAIS execute par l'interpreteur. Python ignore les commentaires.
#

i = 12  # i va faire quelque chose

# Dans Python, il n'y a pas de commentaire de bloc
# Pour commenter un bloc, vous devez commenter chacune des lignes de codes

# NOTE: On a tendance a dire que Python est un langage ou l'on commente enormement. Plus de la moitie du code, sont des
# commentaires. Documentation du code, est a l'interieur du code.
# TOUJOURS: Dites ce que vous faites, et de facon pertinente


#
# 2. Entree et sortie
#

#
# a. Afficher quelque chose
# Pour afficher quelque chose (version simple), on utilise un appel de fonction: print()
#
print("Hello World!")  # Notez Bien: Pour afficher du texte, vous devez le mettre entre guillemets ("), ou entre apostrophes (')
print('Bonjour le monde !')
print(i)  # Va afficher le contenu de la variable# i
print("L'arbre que voici")

print("Voici mes notes de cours")
print("Pour afficher du commentaire, on debute la ligne par un diese # ceci n'est pas un commentaire")

print("Une ligne ", "Un texte", " que dis-je un resultat!")
print("Une liste d'epicerie:\n",  # \n signifie "affiche une nouvelle ligne
      "\t6 oeufs\n",
      "\t1l de lait\n",
      "\t500g de farine\n",
      "\t60g de sucre\n",
      "\t60g de beurre\n",
      "\tEt voila vous avez des crepes !\n")  # \t signifie que vous ajoutez une tabulation
#
# b. Ajouter de l'interactivite en demandant a un utilisateur d'ecrire quelque chose au clavier
#


# input est la fonction qui attend un message de l'utilisateur avec son clavier. Tant que l'utilisateur n'entre pas
# return, input attend.
# Pour memoriser la valeur entree par l'utilisateur (c'est une inconnue), on effectue une assignation.
ret = input("Ecrivez un nombre entre 1 et 100: ")
print("Vous avez ecrit...", ret)  # Affiche le texte, et puis le contenu de la variable ret, donc, ce que l'utilisateur a entre



#
# 3. Chaines de caractere (aka, du texte)
#
"Bonjour"  # Une chaine de caracteres

# Determiner la longueur d'une chaine de caracteres = c'est a dire le nombre de caracteres dans la chaine
# On a une fonction qui s'appelle len()
print(len("Bonjour"))

longueur = len("Bonjour")
print(longueur)


# Exercice: Vous allez demander a un utilisateur d'ecrire un mot dans le clavier et d'appuyer sur Entree. Et puis vous
# allez afficher le nombre de caracteres (ou la longueur) du mot qui a ete entre.
ret = input("Entrez un mot suivi de entree: ")
longueur = len(ret)
print("Vous avez entre un mot de ", longueur, " caracteres.")


# 1. print() - afficher sur la console
# 2. input() - collecter depuis la console un message de l'utilisateur
# 3. len()   - evaluer la longueur d'une chaine de caracteres (entre autres)

print("Good bye")
