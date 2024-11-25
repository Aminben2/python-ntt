class Fournisseur:
    def __init__(self,code,nom,address):
        self.__code = code 
        self.__nom = nom 
        self.__address = address
    
    @property
    def code(self):
        return self.__code
    
    @code.setter
    def code(self,p):
        self.__code = p
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,p):
        self.__nom = p
    
    @property
    def address(self):
        return self.__address
    
    @address.setter
    def address(self,p):
        self.__address = p

    def __str__(self):
        return f"code Fournisseur : {self.code}, nom Fournisseur : {self.nom}, address Fournisseur : {self.address}"
    
    def equals(self,obj):
        return self.nom == obj.nom and self.code == obj.code

class Produit:
    def __init__(self,des,prix,f):
        self.__des = des 
        self.__prix = prix 
        self.__fournisseur = f

    @property
    def des(self):
        return self.__des
    
    @des.setter
    def des(self,p):
        self.__des = p

    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self,p):
        self.__prix = p

    @property
    def fournisseur(self):
        return self.__fournisseur
    
    @fournisseur.setter
    def fournisseur(self,p):
        self.__fournisseur = p

    def __str__(self):
        return f"Désignation Produit : {self.des}, Prix Produit : {self.prix}, Fournisseur : {self.fournisseur}"
    
    def equals(self,obj):
        return self.des == obj.des
    

