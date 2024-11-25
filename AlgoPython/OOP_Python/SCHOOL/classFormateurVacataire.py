from classFormateurs import formateur

# Héritage en Cascade


class formateurVacataire(formateur):
    def __init__(self, ci="0", no='nom', pr='prenom', ane=1900, ar=1999, nh=0):
        self.__NbrH = nh
        formateur.__init__(self, ci, no, pr, ane, ar)

    def getNBH(self):
        return self.__NbrH

    def setNBR(self, nb):
        self.__NbrH = nb

    # Polymorphism
    def afficher(self):
        super().afficher()
        print(f"Nombre heure: {self.__NbrH}")


FV = formateurVacataire("L454", "Ayman", "Akram", 1990, 2012, 150).afficher()
