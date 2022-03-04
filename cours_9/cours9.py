# BABA implementation d'une architecture client serveur
# Serveur cree une socket, ecoute accepte toute requete de connexion
# Il cree une connexion et recoit et envoit des donnees depuis cette connexion
# Client cree une socket, et il se connecte au serveur
# Il utilise pour recevoir et envoyer des donnees

import socketserver

# Programmation orientee object
# Classe
# Instance
# Tous les chevaux partagent les memes traits: Il ressemble a un cheval: criniere, quatre pattes, il hennit
# Notion d'espece cheval: Classe.
# La classe va definir des attributs, et des fonctions (methodes)
class Cheval:
    # __init__ s'Appelle un constructeur
    # Vous allez definir a quoi ressemble le cheval en question
    # En quelque sorte c'Est comme si vous faites naitre un cheval
    def __init__(self, longueur_criniere):
        # self.criniere definit l'Attribut d'un cheval particulier
        self.criniere = longueur_criniere
        self.tete = False

    def hennit(self):
        print("hihihihhihihihihnbrbrbrrbf")
        print("La taille de ma criniere est:", self.criniere)


class Poney(Cheval):
    def hennit(self):
        print("La taille de ma criniere est:", self.criniere)



# Pour instancier (faire naitre un nouveau cheval), on appelle la classe.
# cheval_a = Cheval("courte")
# cheval_b = Cheval("longue")
# poney = Poney("moyenne")


# cheval_a.hennit()
# cheval_b.hennit()
# poney.hennit()


# Un principe de serialisation
# On serialise un fichier sur le reseau, le client deserialise pour enregistrer le fichier
# Cet exemple de telechargement de fichier "a la FTP".
class MonHandlerTCP(socketserver.BaseRequestHandler):
    def handle(self):
        print("Il y a une nouvelle requete")
        data = self.request.recv(4096)
        print("Le client a dit: ", data)
        # Debut de protocole
        # A la commande pswd, transferer sur le reseau le fichier password
        if data == b'pswd':

            # Cette commande pour ouvrir un fichier en mode lecture
            # with open("telechargement.txt", "r") as fichier:

            # Cette commande peut vous etre demandee a l'examen
            with open("passwords.txt", "r") as fichier:
                for line in fichier.readlines():  # Lire un fichier ligne par ligne
                    self.request.sendall(line.encode('utf-8'))  # Chaque ligne est envoyee sur le reseau
                self.request.sendall(b"fini")  # Protocole pour dire que le fichier a ete termine

        # A la commande quit, fermer le serveur
        elif data == b'quit':
            self.finish()

        # Tout autre requete n'est pas supporte par le serveur
        else:
            self.request.sendall(b"Error")





with socketserver.TCPServer(("0.0.0.0", 52000), MonHandlerTCP) as server:
    print("Serveur en attente")
    server.serve_forever()
    print("Au revoir")
