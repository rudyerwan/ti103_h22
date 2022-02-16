# 1. Chaines de caracteres
s = "Lorem Ipsum"
une_autre_variable = "Salut les potes"

print(s)
print(len(s))

# Indexation sur la chaine de caracteres
print(s[0])  # Index 0, sur la chaine de caractere 's', ca va vous retourner le premier caractere de la chaine
print(s[1])  # Deuxieme lettre
print(s[2])

print(s[5])
print(une_autre_variable[4])  # Cinquieme caractere
print(une_autre_variable[6])

# Choisir la derniere lettre
print(s[-1])  # Demander le dernier caractere
print(une_autre_variable[-2])

# La prochaine ligne cause une erreur parce que la chaine de caractere est plus courte que la 26e lettre demandee
# print(s[25])


# Index slicing
print(s[0:5])  # Retourne le 1er, le 2e, le 3e, le 4e et le 5e caractere  => Lorem
print(s[5:-1])  # Retourne une chaine tronquee entre le sizieme caractere et le dernier (non inclus)
print(s[-5:-1]) # Retourne une chaine tronquee entre le cinquieme caractere en partant de la fin et le dernier (non inclus)


# Encore plus fancy. Je veux les caracteres pairs d'une chaine de caracteres
print(s[0:10:2])
print(s[1:11:3])


# Exercice : Une chaine de caractere est trop longue (125 caracteres) pour etre affichee a l'ecran. Donc vous affichez
# les premiers 80 caracteres, et vous affichez le reste.
s1 = "Qu'elle etait verte ma vallee, et j'ai oublie le reste, sinon vous avez des paroles de musique. Cadavre exquis, c'est un exercice de surrealisme."
print(s1[0:80])
print(s1[80:])  # Si vous omettez le nombre apres ':', vous dites a Python "Jusqu'a la fin".


# Trouver l'index
# Dans Python, tout est objet. Un objet a des attributs.
# Par exemple, dans les bases de donnees, un etudiant a un nom, un prenom etc. Nom et prenom sont des attributs
print("Le caractere ' ' est a la position:")
print(s.index(' '))  # ON lui demande l'index d'un espace
print(s.index("o"))

print("Prochaine occurence")
# La prochaine ligne cause une erreur, car il n'y a pas d'espace trouvable a partir du 7e caractere de 'Lorem Ipsum'
# print(s[6:].index(" "))  # On cherche la position de ' ' dans la nouvelle chaine a partir du 7e caractere

# Exercice: Combien de 'm' dans 'Lorem Ipsum'?
print("Il y a tant de 'm' dans 'Lorem Ipsum':")
print(s.count('m'))

# Transformer une chaine de caractere. Mettre tous les caracteres en majuscule
print(s.upper())
print(s.lower())  # Tous les caracteres vont etre en minuscule


# Exercice: On demande a un utilisateur d'entrer son prenom, et on verifie qu'il a entre le prenom "Robert"
# Comme on ne sait pas si l'utilisateur va utiliser une majuscule, on va manipuler la chaine de caractere
prenom = input("Entrez votre prenom (et Entree quand vous avez fini): ")
# Tester la fonction lower()
print("Vous avez entre", prenom.lower())
# Comparer des chaines de caracteres
print(prenom.lower() == 'robert')


# Exercice, afficher mot par mot la chaine de caracteres
# "Salut les potes", Doit retourner => "Salut", "les", "potes"
s = "Salut les potes"
print(s[0:5])   #  [0: 5[
print(s[6:9])   #  [6: 9[
print(s[10:])   #  [10: [
# Mais c'est une solution statique - Elle ne s'adapte, elle ne marche qu'avec "Salut les potes"

print()
print()

s = "Salut les potes"
index_espace = s.index(' ')
print(s[0:index_espace])   # C'est mieux, vous automatisez

s = "Bonjour les potes"
index_espace = s.index(' ')
print(s[0:index_espace])   # C'est mieux, vous automatisez


print(s.split(' '))


# En dehors du cours - Pas d'examen dessus - Tout bonus
print(', '.join(s.split(' ')))


# print(s[0:4], s[6:9], s[10:])


# Longueur de chaines de caracteres
# Indexation pour extraire un caractere particulier
# Slicing pour obtenir une sous chaine d'une chaine de caractere (donc par un exemple un mot)
# Connaitre la position d'un caractere particulier d'une chaine de caracteres
# Compter le nombre de caracteres
# Transformer les chaines : tout en minuscule, tout en majuscule

# Le RPG: vous devez etre capable d'ecrire "Bonjour {NOM_DU_PERSONNAGE}. Comment vas-tu?"
