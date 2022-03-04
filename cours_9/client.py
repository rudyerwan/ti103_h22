import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 52000))
# s.sendall(b"Bonjour serveur")
s.sendall(b"pswd")
while True:
    data = s.recv(4096)
    if data.decode('utf-8') == "fini":
        print("Au revoir")
        break
    if not data:
        break

    # Cette commande pour ouvrir un fichier en mode ecriture
    # with open("telechargement.txt", "w") as fichier:
    # Si vous utilisez le mode "a", vous ecrivez a la fin du fichier

    # Si le fichier n'existe pas, alors il sera automatiquement créé.
    # La commande with fait que le fichier sera correctement ferme en cas d'erreur ou de reussite

    # Cette commande peut vous etre demandee a l'examen
    with open("telechargements.txt", "a") as fichier:
        fichier.write(data.decode("utf-8"))

    # print("Le serveur m'a renvoyé: ", data.decode("utf-8"))
