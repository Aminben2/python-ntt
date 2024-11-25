class Particulier:
    cin = 1

    def __init__(self, n='ayman', ad='kvjv'):
        self.__Nom = n
        self.__Adresse = ad
        self.__CIN = Particulier.cin
        Particulier.cin += 1

    def getNom(self):
        return self.__Nom

    def setNom(self, n):
        self.__Nom = n

    def getAdresse(self):
        return self.__Adresse

    def setAdresse(self, ad):
        self.__Adresse = ad

    def getCIN(self):
        return self.__CIN

    # def ToString(self):
    #     print(f'Nom: {self.__Nom}, CIN: {self.__CIN}, Adresse: {self.__Adresse}')
    def __str__(self):
        return f'CIN: {self.__CIN}, Nom: {self.__Nom}, Adresse: {self.__Adresse}'


class Entreprise:
    def __init__(self, RS="rsrsrsr", C=15.55, NA=152):
        self.__raison_sociale = RS
        self.__capitale = C
        self.__nombre_actions = NA

    def getRS(self):
        return self.__raison_sociale

    def setRS(self, rs):
        self.__raison_sociale = rs

    def getCapital(self):
        return self.__capitale

    def setCaoital(self, c):
        self.__capitale = c

    def getNA(self):
        return self.__nombre_actions

    def setNA(self, na):
        self.__nombre_actions = na

    def Prix_Action(self):
        return f"Valeur d'une action = {self.__capitale/self.__nombre_actions}"

    # def ToString(self):
    #     print(
    #         f"Raison Sociales: {self.__raison_sociale}, Nombres d'actions: {self.__nombre_actions}, Capitale: {self.__capitale}")
    def __str__(self):
        return f"Raison Sociales: {self.__raison_sociale}, Nombres d'actions: {self.__nombre_actions}, Capitale: {self.__capitale}"


class Employé(Particulier):
    mat = 1

    def __init__(self, n='ayman', ad='kvjv', E=Entreprise()):
        super().__init__(n, ad)
        self.__matricule = Employé.mat
        Employé.mat += 1
        self.__entreprise = E

    def getMatricule(self):
        return self.__matricule

    def getEntreprise(self):
        return self.__entreprise

    def setEntreprise(self, e):
        self.__entreprise = e

    def __str__(self):
        return f"{super().__str__()}, Matricule: {self.__matricule}, Entreprise: {self.__entreprise}"


class Cadre(Employé):
    def __init__(self, n='ayman', ad='kvjv', E=Entreprise(), g='a'):
        super().__init__(n, ad, E)
        self.__grade = g

    def getgrade(self):
        return self.__grade

    def setGrade(self, g):
        self.__grade = g

    def __str__(self):
        return f"{super().__str__()}, Grade: {self.__grade}"
