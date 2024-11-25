# Syntax de creation de la class:


class stagiare:
    # Paramétré / d'initialisation:
    def __init__(self, c):
        self.__CEF = c

        # self.__Form = f

    # Les getters / setters (Encapsulation) (Outil):
    def getcef(self):
        return self.__CEF

    # Le comportement membres (méthodes):
    def afficher(self):
        print(
            f"Nom et Prénom: {self.__Nom} {self.__Prenom}s Année de naissance {self.__anaissance} CEF: {self.__CEF}")

    def calculAge(self, anneeActuelle):
        return anneeActuelle - self.__anaissance
