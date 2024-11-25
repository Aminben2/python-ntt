class Compte:
    auto = 1

    def __init__(self, s=0):
        self.__Code = Compte.auto
        self.__Solde = s
        Compte.auto += 1

    # Les getters et le setters
    def getCode(self):
        return self.__Code

    def getSolde(self):
        return self.__Solde

    def setSolde(self, s):
        self.__Solde = s

    # Les méthodes
    def deposer(self, mnt):
        self.__solde += mnt

    def retirer(self, mnt):
        self.__solde -= mnt

    def ToString(self):
        return self.__Solde

    def calculinteret(self, TI):
        self.__Solde += self.__Solde*(TI / 100)


s = float(input("Entrez le solde: "))
C1 = Compte(s)
C2 = Compte()
