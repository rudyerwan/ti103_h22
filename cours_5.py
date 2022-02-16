# J'écris en notation PEP 8
# Vous avez le droit de ne pas mettre d'espace
#par exemple


# 1er exercice
# Introduction sur les séquences
# Boucles, if, comparaison
#
# J'ai une liste de nombres entiers: [5, 4, 8, 2]
# Le but est de trier la liste en ordre croissant
#
# A l'issue de l'exercice on doit obtenir [2, 4, 5, 8]
#
# Triche: Il y a une fonction qui s'appelle: sort
# Le but c'est de le faire par nous meme

l = []  # Une liste vide
l = list()  # Une autre liste vide

l = [5, 4, 8, 2]  # Une liste avec 4 nombres entiers dedans
# La liste se comporte un peu comme une chaine de caracteres
# Liste et chaines de caracteres sont deux structures de donnees 'iterable'
# Donc, on peut indexer une liste
print(l[1])  # Vous retourne le deuxieme element, c'est a dire 4
print(l[2:])  # Vous retourne depuis le troisieme element jusqu a la fin [8, 2]

l.append(9)   # [5, 4, 8, 2, 9] Resultat de append
print(l)
print(l.sort())  # Attention, print rien du tout, sort ne retourne pas la chaine triee
print(l)


l = [5, 4, 8, 2]  # Une liste avec 4 nombres entiers dedans
copy_l = []  # Variable qui va sauvegarder le resultat de l'exercice

# Strategie, on prend chaque element de la liste l, et on l'insere dans la liste copy_l
# Quel est le mot cle pour effectuer une iteration sur un ensemble?
# => Pour chaque element de l
for i in l:
    print(i)   # Affiche les elements de la liste 1 par 1

for i in l:
    copy_l.append(i)
    print(copy_l)

copy_l.clear()
for i in range(5):  # range est comme une liste: range(5) => [0, 1, 2, 3, 4]
    copy_l.append(i)
    print(copy_l)

copy_l.clear()
l = [5, 4, 8, 2]       # Une liste avec 4 nombres entiers dedans

#
# l = [5, 4, 8, 2]
# c = []
#
# l = [5, 4, 8, 2]   le plus petit, le minimum quoi
#               |
#               v
# c =          [2]   J'ai utilise append
# Il faut maintenant eliminer 2 de la liste
# l.remove(2)
# l = [5, 4, 8]
# c = [2]
#
# l = [5, 4, 8]   le plus petit, le minimum quoi
#         |
#         v
# c = [2,  ]   J'ai utilise append


# append: Ajoute a la fin
copy_l.append(min(l))  # Le minimum d'une liste, vous utilisez min()
l.remove(min(l))       # Il va retirer le minimum de l, donc a la fin l = [5, 4, 8]
print(copy_l)

copy_l.append(min(l))  # Le minimum de [5, 4, 8], donc 4
l.remove(min(l))       # Il va retirer le minimum de l, donc a la fin l = [5, 8]
print(copy_l)          # [2, 4]

copy_l.append(min(l))  # Le minimum de [5, 8], donc 5
l.remove(min(l))       # Il va retirer le minimum de l, donc a la fin l = [8]
print(copy_l)          # [2, 4, 5]

copy_l.append(min(l))  # Le minimum de [8], donc 8
l.remove(min(l))       # Il va retirer le minimum de l, donc a la fin l = []
print(copy_l)          # [2, 4, 5, 8]

#
# On vient de copier coller 4 fois le meme code
# Pas tres dynamique
#

# 4 fois la meme chose appelle une boucle
# while = for + if
# while True:    # S'execute toujours tant que la condition est vraie
#     print(":)")

i = 0
while i < 10:
    print("Fais quelque chose")
    i = i + 1

# Meme chose qu'en javascript:
# while (i < 10){
#    console.log("Fais quelque chose");
#    i = i + 1;
# }




l = [5, 4, 8, 2]  # Une liste avec 4 nombres entiers dedans
copy_l = []

# Tant qu'il reste des nombres a trier, je prend le minimum
# et je l'ajoute a ma nouvelle liste copy_l
while l:  # Structure idiomatique: tant que la liste 'l' a des elements dedans
    copy_l.append(min(l))
    l.remove(min(l))
    print("Nouvelle liste:", copy_l)
    print("Ancienne liste:", l)
    print()


# Vous pouvez coder la fonction min
# Donc le but, vous avez une liste, et vous retournez
# le plus petit nombre de la liste.

# Creer une variable x, il faut l'initialiser (lui donner une valeur de depart) - La valeur du premier element de la liste
# Pour chaque element de la liste
# Si l'element est plus petit que la variable x,
# Alors la variable x devient cet element
ll = [4, 2, 3, 1]
# On attend de voir affiche 1 a l'ecran
# Interdiser d'utiliser min
