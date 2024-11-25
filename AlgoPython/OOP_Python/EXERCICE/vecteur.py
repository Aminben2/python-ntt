class Vecteur3d:
    # declaratin de l'attribut stagiaire statique (partagé):
    nb_ins = 0

    # Constructeur:
    def __init__(self, x=0, y=0, z=0):
        self.__X = x
        self.__Y = y
        self.__Z = z
        Vecteur3d.nb_ins += 1

    # Gettdrs / setters:
    def getX(self):
        return self.__X

    def setX(self, dx):
        self.__X = dx

    def getY(self):
        return self.__Y

    def setX(self, dy):
        self.__Y = dy

    def getZ(self):
        return self.__Z

    def setX(self, dz):
        self.__Z = dz

    # les méthodes
    def afficher(self):
        print(
            f"<{self.__X}, {self.__Y}, {self.__Z}>")

    @staticmethod
    def sommeV(V1, V2):
        V = Vecteur3d()
        V.__X = V1.__X + V2.__X
        V.__Y = V1.__Y + V2.__Y
        V.__Z = V1.__Z + V2.__Z
        return V

    def ProduitV(self, V):
        return self.__X * V.__X + self.__Y * V.__Y + self.__Z * V.__Z


# Programme Principale:
V1 = Vecteur3d(5, 8, 3)
V2 = Vecteur3d(3, 8, 4)
V1.afficher()
V2.afficher()
V3 = Vecteur3d.sommeV(V1, V2)
V3.afficher()
print(V1.ProduitV(V2))
