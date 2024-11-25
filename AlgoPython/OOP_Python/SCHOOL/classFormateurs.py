from classMere import personne


class formateur(personne):
    auto = 1

    def __init__(self, ci="0", no='nom', pr='prenom', ane=1900, ar=1999):
        self.__Matricule = formateur.auto
        self.__AnneeR = ar
        formateur.auto += 1
        # personne.__init__(self, ci, no, pr, ane)
        super().__init__(ci, no, pr, ane)

    # Les accessores
    def getMat(self):
        return self.__Matricule

    def getAnnee(self):
        return self.__AnneeR

    def setAnnee(self, ar):
        self.__AnneeR = ar

    # Les méthodes()
    def afficherFormateur(self):
        self.afficher()
        print(
            f"Matricule: {self.__Matricule}, Annee de recrutement: {self.__AnneeR}")

    # Polymorphism
    def afficher(self):
        super().afficher()
        print(
            f"Matricule: {self.__Matricule}, Annee de recrutement: {self.__AnneeR}")
