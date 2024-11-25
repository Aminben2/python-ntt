from cli import client

lst_clt = []
choix = 2
while choix != 6:
    print("""
    1- Ajouter Client:
    2- Afficher tous les clients
    3- Supprimer Client par son nom
    4- Rechercher un client par son nom
    5- Modifier l'adesse d'un client par so nom
    6- Quitter le programme
    """)
    choix = int(input("Entrez votre choix: "))

    if choix == 1:
        nomC = input('Entrez le nom de client: ')
        adrs = input('Entrez l\'adresse de client: ')
        C = client(nomC, adrs)
        lst_clt.append(C)
    elif choix == 2:
        for i in lst_clt:
            print(i.ToString())
    elif choix == 3:
        nmc = input("Etrez le nom du client supprimer: ")
        for i in lst_clt:
            if i.getNom() == nmc:
                exist = True
                lst_clt.remove(i)
            if not(exist):
                print("Ce client n'existe pas")
    elif choix == 4:
        nmc = input("Entrez le nom du client à rechercher: ")
        exist = False
        for i in lst_clt:
            if i.getNom() == nmc:
                exist = True
                clt = i
            if not(exist):
                print("Ce client n'existe pas")
            else:
                print(f"Ce client existe: {clt.ToString()}")
    elif choix == 5:
        nmc = input("Etrez le nom du client à modifier: ")
        exist = False
        for i in lst_clt:
            if i.getNom() == nmc:
                exist = True
                i.setAdresse(input("Entrez la nouvelle adresse: "))
            if not(exist):
                print("Ce client n'existe pas")
    elif choix == 6:
        print("Fin Programme")
    else:
        print("Choix Invalid")
