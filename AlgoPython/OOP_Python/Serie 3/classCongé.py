from datetime import date


class Employé:
    def __init__(self, n="nom", p="pre", mat=5, d=date(2018, 5, 10), sold=515):
        self.__Nom = n
        self.__Prenom = p
        self.__Matricule = mat
        self.__DateC = d
        self.__Sold = sold

    @property
    def Nom(self):
        return self.__Nom

    @Nom.setter
    def Nom(self, n):
        self.__Nom = n

    @property
    def Prenom(self):
        return self.__Prenom

    @Prenom.setter
    def Prenom(self, n):
        self.Prenom = n

    @property
    def Matricule(self):
        return self.__Nom

    @Matricule.setter
    def Matricule(self, n):
        self.__Matricule = n

    @property
    def DateCongé(self):
        return self.__Nom

    @DateCongé.setter
    def DateCongé(self, n):
        self.__DateC = n

    @property
    def Solde(self):
        return self.__Sold

    @Solde.setter
    def Solde(self, n):
        self.__Sold = n

    def __str__(self):
        return f"Nom: {self.__Nom}, Prénom: {self.__Prenom}, Matricule: {self.__Matricule}, Date de congé: {self.__DateC}, Solde: {self.__Sold}"


class Manager(Employé):
    def __init__(self, n="nom", p="pre", mat=5, d=date(2018, 5, 10,), sold=515, lst=[]):
        super().__init__(n, p, mat, d, sold)
        self.__lstEmployé = lst

    def __str__(self):
        return f"{super().__str__()}"

    def listEmployé(self):
        for i in self.listEmployé:
            print(i)

    def ajouterEmployé(self, E):
        if E in self.__lstEmployé:
            print('Employé existe deja')
        else:
            self.__lstEmployé.append(E)

    def getEmployébyCode(self, c):
        exist = False
        for i in self.__lstEmployé:
            if i.Matricule == c:
                exist = True
        if exist == False:
            print("Employé n'existe pas")
        else:
            print(i)


class DemandeCongé:
    etat = "En cours"

    def __init__(self, c=0, d=date(2018, 5, 10), dr=2, motif="vdoj"):
        self.__Code = c
        self.__DateD = d
        self.__Duree = dr
        self.__Motif = motif
        self.__Etat = DemandeCongé.etat

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, n):
        self.__Code = n

    @property
    def DateD(self):
        return self.__DateD

    @DateD.setter
    def DateD(self, n):
        self.__DateD = n

    @property
    def Duree(self):
        return self.__Duree

    @Duree.setter
    def Duree(self, n):
        self.__Duree = n

    @property
    def Motif(self):
        return self.__Motif

    @Motif.setter
    def Motif(self, n):
        self.__Motif = n

    @property
    def Etat(self):
        return self.__Etat

    @Etat.setter
    def Etat(self, E):
        self.__Etat = E

    def Valider(self):
        self.Etat = "Valider"

    def Refuser(self):
        self.Etat = "Refuser"


class GestionCongé:
    def __init__(self, lstManager=[], lstDemande=[]):
        self.__lstManager = lstManager
        self.__lstDemande = lstDemande

    def ajouterDemandeCongé(self, ObjDemande):
        if ObjDemande in self.__lstDemande:
            print("Demande deja axiste")
        else:
            self.__lstDemande.append(ObjDemande)

    def listeDemandeCongéEnCour(self):
        lst = []
        for i in self.__lstDemande:
            if i.Etat == "En cours":
                lst.append(i)
        return lst

    def listedemandeCongéParEmploye(self, code):
        lst = []
        for i in self.__lstDemande:
            if i.Code == code:
                lst.append(i)
        return lst
