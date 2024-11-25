class Auteur:
    def __init__(self, nom="moad", natio="marocain"):
        self.__nom = nom
        self.__natio = natio

    def getnom(self):
        return self.__nom

    def getnatio(self):
        return self.__natio

    def setnom(self, nom):
        self.__nom = nom

    def setnatio(self, natio):
        self.__natio = natio

    def AfficherAuteur(self):
        print(f"Nom: {self.__nom},Nationalite: {self.__natio}")


class Livre:
    def __init__(self, nom="dhhdgf", editor="kdcvh", nbp=500, l_a=Auteur()):
        self.__nom = nom
        self.__editor = editor
        self.__nbp = nbp
        self.__l_a = l_a

    def getNom(self):
        return self.__nom

    def setNom(self, n):
        self.__nom = n

    def getEditor(self):
        return self.__editor

    def setEditor(self, e):
        self.__editor = e

    def getNbP(self):
        return self.__nbp

    def setNbP(self, nb):
        self.__nbp = nb

    def getl_a(self):
        return self.__l_a

    def setl_a(self, l_a):
        self.__l_a = l_a

    def AfficherAuteurlivres(self):
        for i in self.__l_a:
            i.AfficherAuteur()

    def AjouterAuteur(self, A):
        self.__l_a.append(A)

    def ajouterAuteur(self):
        nom = input("Entrez le nom de l'auteur: ")
        nat = input("Entrez la nationalité de l'auteur: ")
        A = Auteur(nom, nat)
        self.__l_a.append(A)

    def SupprimerAuteur(self, A):
        for i in self.__l_a:
            if A in self.__l_a:
                self.__l_a.remove(i)
            else:
                print("Cet auteur n'existe pas")

    def SupprimerAuteur(self, nomAuteur):
        exist = False
        for i in self.__l_a:
            if i.getnom() == nomAuteur:
                exist = True
                Livre.LstAuteur.remove(i)
            if not(exist):
                print("Cet auteur n'existe pas")

    def AfficherLivre(self):
        print(
            f"Nom: {self.__nom} -Editor: {self.__editor} -Nombre Page: {self.__nbp}")
        print("la liste de cet auteur sont: ")
        self.AfficherAuteurlivres()


class Biblio:
    def __init__(self, nom="biblio", adresse="sdfg", L=Livre()):
        self.__nom = nom
        self.__adresse = adresse
        self.__L = L

    def getNom(self):
        return self.__nom

    def setNom(self, nb):
        self.__nom = nb

    def getAd(self):
        return self.__adresse

    def setAd(self, ad):
        self.__adresse = ad

    def getL(self):
        return self.__L

    def setL(self, L):
        self.__L = L

    def AfficherLivreBiblio(self):
        for i in self.__L:
            i.AfficherLivre()

    def AjouterLivre(self):
        noml = input("Entrez le nom de livre: ")
        ed = input("Entrez l'editor' de livre: ")
        nbp = int(input("Entrez le nombre des pages de livre: "))
        L = Livre(noml, ed, nbp)
        nba = input("Entrez le nombre des auteurs")
        for i in range(nba):
            L.ajouterAuteur()
        self.__L.append(L)

    def ajouterLivre(self, S):
        self.__L.append(S)

    def SupprimerLivre(self, L):
        if L in self.__L:
            self.__L.remove(L)
        else:
            print("Ce livre n'existe pas")

    def supprimerLivre(self, nomLivre):
        exist = False
        for i in self.__l_a:
            if i.getnom() == nomLivre:
                exist = True
                self.__L.remove(i)
            if not(exist):
                print("Ce livre n'existe pas")

    def AfficherBiblio(self):
        print(f"Nom: {self.__nom} -Adresse: {self.__adresse}")
        print("Ces livres sont: ")
        self.AfficherLivreBiblio()


# Programme principale:
A1 = Auteur("moad", "marocain")
A2 = Auteur("ayman", "marocain")
A3 = Auteur("Akrami", "Tunisien")
L1 = Livre("PHP", "Nathan", 100, [A1, A2])
L2 = Livre("JAVA", "Marc", 200, [A1])
L3 = Livre("PHP", "Nathan", 100, [A1, A2, A3])
B = Biblio("Bib ISMO", "Ismo", [L1, L2, L3])
print("1\n")
B.AfficherBiblio()
print("2")
B.AjouterLivre()
print("3")
B.SupprimerLivre(input("Entrez le nom du livre à supprimer: "))
print("4")
nom1 = input("Entrez le nom de livre que voulez modifier")
for i in B.getL():
    if i.getNom() == nom1:
        i.AjouterAuteur()
print("5")
B.AfficherBiblio()
