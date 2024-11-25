from abc import ABCMeta, abstractmethod


class languagueProgrammation(metaclass=ABCMeta):
    # La méthode abstraite:
    @abstractmethod
    def isPOO(self):
        pass


class Python(languagueProgrammation):
    # Redifinition de la methode abstraite
    def isPOO(self):
        return True


class C(languagueProgrammation):
    def isPOO(self):
        return False


P = Python()
print(P)
