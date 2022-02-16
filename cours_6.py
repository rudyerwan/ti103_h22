# Rappel - Bien faire correspondre un outil a un besoin
# Pour chaque element de: ca doit appeler, une boucle for
# Tant qu'une condition est vraie, fais ceci: ca doit appeler, une boucle while
# while condition:
#    action a executer en boucle
#
# for quelque chose dans une sequence:
#    action a executer en boucle

# Une boucle de jeu - (game loop)
# Une boucle qui se repete toujours
# while True:
#     est-ce que le joueur a appuye une touche
#     est-ce que le joueur a clique pour fermer la fenetre
#        si oui: on sort du programme
#     si non
#        on reaffiche les nouveaux elements dans la fenetre de jeu



# Soit une liste d'entiers non tries.
l = [12, 4, -5, -19, 0, 13, 49]


mon_minimum = l[0]

# Pour chaque element i de la liste l
for i in l:
    # l[0] => i, i = 12
    # l[1] => i, i = 4
    # l[2] => i, i = -5
    # ...
    #

    # Si mon nouvel element i est plus petit que la valeur memorise (mon_minimum)
    if i < mon_minimum:
        # Alors, i va devenir la nouvelle valeur memorisee
        mon_minimum = i
        # raise Exception("Badaboom")


print("Le minimum de", l, "est", mon_minimum)


import cours_6_b
cours_6_b.ma_premiere_fonction(1)  # On appelle une fonction




# Exercice - L'ordinateur choisit un nombre aleatoire entre 1 et 100
# Il demande au joueur de deviner le nombre, et il dit plus grand ou petit
# Challenge: Si le joueur n'a pas devine le bon nombre au bout de 5 fois, et ben, il perd.
import random

valeur_a_trouver = random.randint(1, 100)
i = 0
# gagne = False

while True:  # i <= 5:  # (alternative 3)
    # Alternative 1
    if i >= 5:
        print("Vous avez perdu, vous n'avez pas trouve en 5 fois")
        break

    x = input("Jeu (mais sans argent). Veuillez entrer un nombre entier entre 1 et 100: ")
    x = int(x)  # On pense a transformer la chaine de caractere retournee par input, en un nombre entier
    i += 1  # i++ javascript, C, java, i= i + 1 - Incrementeur, accumulateur

    if x < valeur_a_trouver:
        print("Plus grand")
    elif x > valeur_a_trouver:  # else if de javascript
        print("Plus petit")
    else:
        print("Bien joue mon grand, tu as gagne en", i, "coups.")
        # gagne = True
        # print(f"Bien joue mon grand, tu as gagne en {i} coups.")   # f-strings

        # Le joueur a gagne, plus besoin de boucler, on sort du jeu
        break

    # Alternative 2
    # if i > 5:
    #     print("Vous avez perdu, vous n'avez pas trouve en 5 fois")
    #     break

# if not gagne:
#     print("Vous avez perdu, vous n'avez pas trouve en 5 fois")


#
# Exercice - On demande a un utilisateur d'entrer une chaine de caractere
# On lui dit si sa chaine de caractere a au moins deux caracteres au moins en double
# Par exemple:
# Si l'utilisateur ecrit 'Bonjour' => 'o' apparait deux fois. Donc, vous ecrivez "vrai"
# Si l'utilisateur ecrit 'Abcdefs' => Aucun caractere n'apparait deux fois. Donc, vous ecrivez "faux"
#
# Python: dictionnaire.
# { 'rouge': rgb(255, 0, 0) };
# { 'B': 1, 'o': 2, 'n': 1 ... }