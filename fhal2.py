class Auteur:
    def __init__(self,nom,nat):
        self.__nom = nom
        self.__nationalite = nat
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,p):
        self.__nom = p

    @property
    def nationalite(self):
        return self.__nationalite
    
    @nationalite.setter
    def nationalite(self,p):
        self.__nationalite = p
    
    def __str__(self):
        return f"Autheur nom : {self.nom} , Autheur Nationalite : {self.nationalite}"

class Livre:
    def __init__(self,nom,editor,nb,listAuteur):
        self.__nom = nom
        self.__editor = editor
        self.__nb_pages = nb 
        self.__list_autheurs = listAuteur

    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self,p):
        self.__nom = p

    @property
    def editor(self):
        return self.__editor
    
    @editor.setter
    def editor(self,p):
        self.__editor = p

    @property
    def nb_pages(self):
        return self.__nb_pages
    
    @nb_pages.setter
    def nb_pages(self,p):
        self.__nb_pages = p

    @property
    def list_autheurs(self):
        return self.__list_autheurs
    
    @list_autheurs.setter
    def list_autheurs(self,p):
        self.__list_autheurs = p


    def AfficheAuteursLivres(self):
        if len(self.list_autheurs) : print("No Autheurs !"); return
        for i in self.list_autheurs:
            print(i)
        
    def AjouterAuteur(self,a):
        if isinstance(a,Auteur) :
            check = False 
            for i in self.list_autheurs:
                if i.nom == a.nom: check = True ; break
            if not check :
                self.list_autheurs.append(a)
        else :
            print("Provide a Autheur")

    def AjouterAuteur(self):
        a = Auteur()
        nom = input("Enter nom : ")
        nat = input("Enter Nationalite : ")
        a.nom = nom
        a.nationalite = nat
        self.AjouterAuteur(a)

    def Supprimer( self,a):
        if isinstance(a,Auteur) :
            check = False 
            tmp = self.list_autheurs[:]
            for i in range(len(tmp)):
                if tmp[i].nom == a.nom:
                    check = True 
                    del self.list_autheurs[i]
                    break
            if not check :
                print("Autheur not found/ could not delete it")
        else :
            print("Provide a Autheur")

    def Supprimer( self,a):
        check = False 
        tmp = self.list_autheurs[:]
        for i in range(len(tmp)):
            if tmp[i].nom == a:
                check = True 
                del self.list_autheurs[i]
                break
        if not check :
            print("Autheur not found/ could not delete it")

    def AfficheLivre(self):
        print(f"Nom livre : {self.nom}, Editor : {self.editor}, Nombre de pages : {self.nb_pages}")
        print("Liste d'autheurs")
        for i in self.list_autheurs:
            print(i)
    
