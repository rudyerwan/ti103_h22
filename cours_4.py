#
# Exercice - Demande a un utilisateur d'entrer un nombre entier quelconque
#            Et on lui affiche a l'ecran si le nombre est pair, ou si le nombre est impair
#            Et en plus, on lui dit si le nombre est inferieur a 10
#
# Modulo 2 - parite d'un nombre
# 0 = 0x2 + 0
# 1 = 0x2 + 1
# 2 = 1x2 + 0
# 3 = 1x2 + 1
# 4 = 2x2 + 0
# 5 = 2x2 + 1
#
# Modulo est exprime par l'operateur '%'
# 0 % 2 = 0
# 1 % 2 = 1
# 2 % 2 = 0
# 3 % 2 = 1
# 4 % 2 = 0
# 5 % 2 = 1
#
# Recapitulatif - divisions, et partie entiere
# 17    3 * 5 + 2   3 * 5   2       2  <- reste
# -- =  --------- = ----- + - = 3 + _   |
#  5        5         5     5       5   |
#                               ^       |
# 17 // 5 = 3 ------------------+       |
# 17 %  5 = 2 --------------------------+
#
# 19   9 * 2 + 1   9 * 2   1       1  <- reste non nul, donc, il est impair
# -- = --------- = ----- + _ = 9 + _
#  2       2         2     2       2
#
# 19 // 2 = 9
# 19 % 2 = 1 <- residu, reste, donc ce n'est pas un multiple de 2, donc ce n'est pas pair
# y % 2 = ...
#
y = input('veuillez entrer un nombre entier')
y = int(y)
if y % 2 == 0:
    print('cest un nombre pair')
if y % 2 == 1:
    print('cest un nombre impair')
if y < 10:
    print('inferieur a 10')


# Exercice - Demander a un utilisateur de donner un nombre entier quelconque
#            On lui retourne si le nombre est premier
#
# Un nombre premier - divisible par 1 ou par lui meme, qui n'est pas 1, et 0 n'est pas premier
#
# Un algorithme simple :
# Vous divisez le nombre (x) par deux et l'assignez a une autre variable (y = x / 2)
# Pour chaque nombre z de 2 a y
# Vous divisez le nombre x par z, et si le reste est 0, alors il est multiple de z, il n'est pas premier
#
# x = 7
# y = 4  (7 / 2 = 3.5 alors j'arrondis a l'entier superieur)
#
# Boucle:
# z = 2
# x / z = 7 / 2 = (3*2+1)/2 = 3 + 1/2, il y a un reste, donc ce n'est pas un multiple
# z = 3
# x / z = 7 / 3 = (2*3+1)/3 = 2 + 1/3, il y a un reste, donc ce n'est pas un multiple
# z = 4
# x / z = 7 / 4 = (1*4+3)/4 = 1 + 3/4, il y a un reste, donc ce n'est pas un multiple
#
# On est arrive a y, on s'arrete, 7 n'a pas de diviseur entre 2 et 4. Il est donc premier
#
# x = 8
# y = 4  (8 / 2)
# Boucle:
# z = 2
# x / z = 8 / 2 = (4*2+0)/2 = 4 + 0/2, il n'y a pas de reste, donc c'est un multiple
# Et si il y a un diviseur entre 2 et 4, alors, ce n'est pas un nombre premier
x = input("Veuillez entrer un nombre premier: ")
x = int(x)
y = x // 2 + 1  # On veut un entier et on arrondit a l'entier superieur

flag = False

if x == 0 or x == 1:
    print("Ce nombre n'est pas premier")
    flag = True

# for: cree une boucle
# On veut une boucle entre 2 et y/2 => on va utiliser la fonction range
# range(2, 5) en mathematique = [2, 5[, de 2 inclus a 5 exclus
for i in range(2, y):
    if x % i == 0:
        print("Ce nombre n'est pas premier")
        flag = True
        break  # On sort de la boucle for immediatement,

if flag == False:
    print("Ce nombre est premier")


# Exercice - Si le nombre n'est pas premier, donner la preuve. Dites quel est le diviseur que
# vous avez trouve
# Afficher a l'ecran la variable 'i'