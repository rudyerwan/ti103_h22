
entree_utilisateur = input("Veuillez entrer une chaine de caracteres: ")


# Utilisateur entre la phrase: 'Bonjour le monde'
# Structure de donnees dans Python: Le dictionnaire
# Un ensemble de cle et de valeurs (map en javascript?)
# On pourrait eventuellement fabriquer une base de donnees avec des dictionnaires
# Etudiant:
# Nom
# Prenom
# Numero_etudiant
#
# d = {'nom': 'Huberdeau', 'prenom': 'Alex', 'Numero_etudiant': 0}
# e = {'nom': 'Fowang', 'prenom': 'John', 'Numero_etudiant': 1}
#
# print(d['nom']) => 'Huberdeau'
# print(d['prenom']) => 'Alex'
# d['prenom'] = 'alex'


#for lettre in entree_utilisateur:
#    if lettre in ...
#        incremente compteur
#    else
#        cree une nouvelle cle dans le dictionnaire

d = {}  # Assigne un dictionnaire vide a la variable d ({} pour les dictionnaires, et les set)
for lettre in entree_utilisateur:
    if not lettre in d:
        d[lettre] = 1

    elif lettre in d:
        # l[2] -> Accede au deuxieme element de la liste (ou eventuellement de la chaine de caracteres)
        d[lettre] += 1

print(d)
for cle in d.keys():
    if d[cle] > 1:
        print("Vous avez affiche la lettre ", cle, d[cle], " fois")
