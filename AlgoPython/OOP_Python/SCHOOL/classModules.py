from classFormateurs import formateur


class Module:
    auto = 1
    # Constructeur:

    def __init__(self, nm="M01", mh=0, f=formateur()):
        self.__IdM = Module.auto
        Module.auto += 1
        self.__NomM = nm
        self.__Formateur = f
        self.__MH = mh

    def getId(self):
        return self.__IdM

    def getNom(self):
        return self.__NomM

    def setId(self, n):
        self.__NomM = n

    def getMh(self):
        return self.__MH

    def setIMh(self, m):
        self.__MH = m

    def getF(self):
        return self.__Formateur

    def setF(self, f):
        self.__Formateur = f

    def Infos(self):
        print(
            f"-Nom modules: {self.__NomM} -Enseigné par: {self.__Formateur.afficher()} -Mass horaire: {self.__MH}")


M1 = Module()
# M1.Infos()
F1 = formateur()
F2 = formateur("Ahmadi", "Ahmad", 2019)
M2 = Module("M02", F1, 100)
M3 = Module("M03", F2, 120)
# M3.Infos()
M4 = Module("M04", formateur("fatmi", "fatima", 2000), 90)
