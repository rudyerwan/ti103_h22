# 1. Les variables
#
# En mathematique - Le terme le plus proche: une inconnue
# x, y, z en math f(x,y) = 2x + 3y
# On assigne des valeurs aux variables
# La premiere fois qu'on definit une variable, on lui assigne une valeur

# Une variable qui se promene toute seule, comme: a
# Ca signifie que Python lit la valeur

# Assignation: NOM_VARIABLE = VALEUR, x = 12
x = 1  # Assignation - Variable toujours a gauche de l'egalite, la valeur toujours a droite
# 1 = 1  # Comparaison entre deux valeurs


# L'operateur pour assigner '='
# L'operateur pour comparer, et verifier une egalite: '=='
# 1 == 1
y = 0

z = 5 + 9
z = x - y  # S'evalue a 1 - 0

# Pour multiplier: *
z = x * y
z = x * 4
print(z)
# z = x - a  # NameError: name 'a' is not defined, ca signifie que vous chercher a lire la valeur d'une variable non definie

strength = 1
wisdom = 1
intelligence = 1
hit_points = 100

# Nommage de variable
# Tous les caracteres alpha numeriques 0 1 2 3 4 5 6 7 8 9 a z
# Le premier caractere d'une variable ne peut pas etre un chiffre
tatayoyo = 12
tatayoyo12 = 534
tata23yoyo = 7645
# 1tatayoyo = 67
# tata-yoyo = 34  # Caracteres d'operation
# Le caractere de barre souligne: _ il est permis, car il remplace ' '
# tata yoyo = 12  # Interdit, pas d'espace pour nommer une variable
tata_yoyo = 12
tatayoyo___ = 4553
_tatayoyo = 234  # Information, ca declare une intention, style de programmation

# La convention pour les variables
ma_premiere_variable = 12

maPremiereVariable = 14  # Valable (info: mais considere comme une erreur de style) on se prend pas la tete
mapremierevariable = 16
MA_PREMIERE_VARIABLE = 15  # Permis aussi.

# Les trois dernieres variables sont toutes differentes

# Les variables toute en chaine de caractere = Exprime une intention - Constante
PI = 3.141592654   # Vous declarez, vous promettez que JAMAIS le programme change la valeur de pi
C = 3000000        # km.s-1

LEVEL_MAX = 100


# 2. TYPAGE
# Python - typage dynamique fort
# typage dynamique = nul besoin de definir le type de la variable
# C: typage statique:   int t = 12;

# Exercice - On demande a l'utilisateur d'entrer deux nombres entiers (quelconques)
# On affiche le produit des deux

# Declarer deux variables
# Une troisieme variable qui stocke la somme des deux premieres variables
# Print la troisieme variable
s = input("Entrer un premier nombre entier: ")

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
# Corollaire - La fonction input retourne TOUJOURS une chaine de caracteres
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

# Pour tester un type, on utilise une fonction qui s'appelle type()
print(type(s))   # Ca retourne 'str', ca signifie que c'est une chaine de caracteres

# Le type de la variable, en mathematique, c'est le domaine

# Et comme les chaines de caracteres acceptent l'operateur '+', ca marche, mais en
# fait ca concatene les chaines de caracteres: Donc "3" + "4" = "34", et 3 + 4 = 7

# Pour transformer un type, on appelle des fonctions
# Par exemple: de chaine de caracteres a nombre entiers: int()
# Par exemple: de nombre entier a chaine de caracteres: str()
# Par exemple: de chaine de caracteres a nombre decimaux: float()
s = int(s)

t = input("Entrer un deuxieme nombre entier: ")
t = int(t)  # y = int(t) est tout aussi valable. t= int(t) auto reassignation

u = s + t   # L'operateur + de deux entiers, va devenir une addition
print(u)

# PEP 8
# str()