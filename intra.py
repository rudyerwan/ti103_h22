# Question 1

# 1. demande à un utilisateur d’écrire au clavier le chemin pour ouvrir un fichier.
chemin = input("Veuillez entrer le chemin vers le fichier: ")

# 2. choisit un nombre entier au hasard et écrit ce nombre dans le fichier.
import random

nombre = random.randint(0, 100)

with open(chemin, "w") as f:
    nombre = str(nombre)
    f.write(nombre)

# 3.affiche à l’écran le nombre qui a été écrit dans le fichier.
print(nombre)


import time
def carre_lent(a):
    time.sleep(10)
    return a ** 2   # pow(a, 2) = a a la puissance 2


# Question 2
#1.Définit un nouveau dictionnaire ‘d’
d = {}


#2.Définit une nouvelle fonction ‘carre_cache’:
#a)La fonction accepte un paramètre ‘a’
def carre_cache(a):
    print("Le parametre a entre dans carre cache est de: ", a)
    #b)Si ‘a’ est dans le dictionnaire ‘d’, retourner la valeur correspondante
    if a in d:
        print("Valeur deja en cache")
        return d[a]
    #c)Sinon
    else:
        print("Valeur pas en cache. Je vais la chercher...")
        #i.Exécuter carre_lent(a)
        #ii.Ajouter le résultat de carre_lent(a) dans le dictionnaire ‘d’
        res = carre_lent(a)
        d[a] = res
        # Si carre_cache(12)  # J'ai choisi 12 arbitrairement
        # d[12] = 144 (valeur retournee de carre_lent)

        # cle - valeur
        # Donnez cle => retourne la valeur
        # Assignez a une cle en donnant une valeur
        # d['nom'] = 'yannick'
        #print(d['nom'])

        #iii.Et retournez le résultat de carre_lent(a)
        return res


carre_cache(1)
carre_cache(2)
carre_cache(1)


# Question 3
#1.Écrivez une fonction nommée ‘digit’ qui
#a)accepte deux paramètres: a et b,
def digit(a, b):
    #b)et retourne  a * 60b   (rappel: xy = pow(x, y) en python)
    return a * pow(60, b)

#2.Créez une liste ‘l’ qui contient les valeurs suivantes: 6, 16, 59, 28, 1, 34, 51, 46, 14, 50
l = [6, 16, 59, 28, 1, 34, 51, 46, 14, 50]

#3.Définissez une variable ‘diamètre’
diametre = 0

#4.Faites une boucle qui fait la somme:
#a)Pour i variant de 0 à 9 (inclus)
for i in range(0, 10):
    #b)Assigne à une variable x la valeur de la liste ‘l’ à l’index I
    x = l[i]
    #c)Ajoute au diamètre le résultat de digit(x, -i)
    diametre += digit(x, -i)

#5.N’oubliez pas de diviser le ‘diamètre’ par deux et afficher le résultat
diametre = diametre / 2
print(diametre)
