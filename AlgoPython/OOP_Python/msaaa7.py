from abc import ABCMeta,abstractmethod
from http import client
from re import M
class Voiture:
    def __init__(self,mat="1534",marq="nissan",carb="diesel",mod=2021,pf=112):
        self.__Matricule=mat
        self.__Marque=marq
        self.__Carburant=carb
        self.__Modele=mod
        self.__PuissF=pf
    #getters 
    def getMat(self):
        return self.__Matricule
    def getMarq(self):
        return self.__Marque
    def getCarb(self):
        return self.__Carburant
    def getModel(self):
        return self.__Modele
    def getPuiss(self):
        return self.__PuissF
    #setters
    def setMat(self,mat):
        self.__Matricule=mat
    def setMarq(self,marq):
        self.__Marque=marq
    def setCarb(self,carb):
        self.__Carburant=carb
    def setModele(self,mod):
        self.__Modele=mod
    def setPuiss(self,pf):
        self.__PuissF=pf
    #__str__
    def __str__(self):
        return f"matricule:{self.__Matricule},marque:{self.__Marque},Carburant:{self.__Carburant},model:{self.__Modele},puissance:{self.__PuissF}"
    
    def Ajouter(self,LV,V):
        if V in LV:
            print("deja existant")
        else:
            LV.append(V)
    def Supprimer(self,LV,m):
        for i in LV:
            if i.getMat==m :
                LV.remove(m)
            else:
                print("n'est pas existe")
    def modifier(self,LV,m):
        for i in LV:
            if i.getMat==m:
                setMat=int(input("entre lAa nouvelle matricule"))
                setMarq=input("entre la nouvelle marque")
                setCarb=input("entre la nouvelle carb")
                setModele=int(input("entre la nouvelle modele"))
                setPuiss=int(input("entre la nouvelle puiss"))
            else:
                print("aucun matricul")
class VoitureVip:
    def __init__(self,tp="SUV"):
        self.__Type=tp
    #getters setter
    def getType(self):
        return self.__Type
    def setType(self,tp):
        self.__Type=tp
    def __str__(self):
        return f"le type:{self.__Type}"
class VoitureCitadinne:
    def __init__(self,g="B"):
        self.__Gamme=g
    #get set
    def getGamme(self):
        return self.__Gamme
    def setGamme(self,g):
        self.__Gamme=g
    def __str__(self):
        return f"La gamme:{self.__Gamme}"
class Client:
    def __init__(self,nump=451,tel=242409097):
        self.__NumP=nump
        self.__Tele=tel
    #get 
    def getNumP(self):
        return self.__NumP
    def getTele(self):
        return self.__Tele
    #set
    def setNumP(self,nump):
        self.__NumP=nump
    def setTele(self,tel):
        self.__Tele=tel
    def __str__(self):
        return f"num Permis:{self.__NumP},Tele:{self.__Tele}"
    def ajouter(self,LC,C):
        if C in LC:
            print("deja existant")
        else:
            LC.append(C)
    def Supprimer(self,LC,np):
        for i in LC:
            if i.getNumP==np:
                LC.remove(np)
            else:
                print("n'est pas existe")
    def modifier(self,LC,NP):
        for i in LC:
            if i.getNumP==NP:
                setNumP=int(input("entre lAa nouvelle Nump"))
                setTele=int(input("entre la nouvelle Numero"))
    ######methodesss????????????/
from datetime import date
from datetime import time
class Location(Voiture,Client):
    idL=1
    def __init__(self,dtl=date(1111,11,1),drl=date(2222,2,2),c=client(),pr=9879,v=Voiture()):
        self.__dl=dtl
        self.__dr=drl
        self.__idL=Location.auto
        Location.auto+=1
        self.__cl=c
        self.__prix=pr
        self.__vo=v
    @property
    def dl(self):
        return self.__dl
    @property
    def idl(self):
        return self.__idL
    @ dl.setter
    def dl (self,d):
        self.__dl=d
    @property
    def dr(self):
        return self.__dr
    @ dr.setter
    def dr (self,d):
        self.__dr=d
    @property
    def cl(self):
        return self.__cl
    @ cl.setter
    def cl (self,d):
        self.__cl=d
    @property
    def prix(self):
        return self.__prix
    @ prix.setter
    def dl (self,d):
        self.__prix=d
    @property
    def vo(self):
        return self.__vo
    @ vo.setter
    def vo (self,d):
        self.__vo=d
    def __str__(self):
        return f"idlocation est{self.__idL} date de locetion{self.__dl} duree de location{self.__dr} voiture {self.__vo} client {self.__cl}  "


class Utilisateur:
    def __init__(self,l="fghj",mp=0,E="sdf"):
        self.__mp=mp
        self.__e=E
        self.__l=l
    @property 
    def l(self):
        return self.__l
    @l.setter
    def l(self,l):
        self.__l=l
    @property 
    def e(self):
        return self.__e
    @e.setter
    def e(self,l):
        self.__e=l
    @property 
    def mp(self):
        return self.__mp
    @mp.setter
    def mp(self,l):
        self.__mp=l
    

class ListeUtilisateurs:
    def __init__(self,LU=[]):
        self.__LU=LU
    @property
    def LU(self):
        return self.__LU
    @LU.setter
    def LU(self,lu):
        self.__LU=lu
    def authentifier(self,login,m):
        for i in self.__LU:
            if i.Utilisateur.l==login and i.Utilisateur.mp==m:
                print("bonjour")
            else:
                print("n'existe pas")
    def ajouter(self,u):
        if u in self.LU:
            print("deja existe ")
        else:
            self.__LU.append(u)
    def Supprimer(self,login):
        for i in self.__LU:
            if i.l==login:
                self.__LU.remove(login)
            else:
                print("n'est pas existe")
    def Modifier(self,u):
        for i in self.__LU:
            if i==u:
                l=input("entre le nouveau login")
                mp=input("entre le nouveau mot de passe ")
class Personne:
    def __init__(self,cin=0,Nom="moussaoui",prenom="manal"):
        self.__nom=Nom
        self.__prenom=prenom
class ListeLocations:
    def __init__(self,LL=[]):
        self.__LL=LL
    @property
    def LL(self):
        return self.__LL
    @LL.setter
    def LL(self,l):
        self.__LL=l
    def AfficherListeLocation(self):
        for i in self.__LL:
            print(i)
    def AfficherListeLocation(self):
        l=[]
        for i in self.__LL:
            if isinstance(i,VoitureCitadinne)==True:
                l.append(i)
    def AfficherListeLocationVip(self):
        lv=[]
        for i in self.__LL:
            if isinstance(i,VoitureVip)==True:
                lv.append(i)
    def AfficherLocationMarque(self,m):
        lm=[]
        for i in self.__LL:
            if i.Voiture.getMarq==m:
                lm.append(i)
    def AfficherLocationImma(self,im):
        lim=[]
        for i in self.__LL:
            if i.Voiture.getMat==im:
                lim.append(i)
    def AfficherLocationClient(self,np):
        lc=[]
        for i in self.__LL:
            if i.Client.NumP==np:
                lc.append(np)
    def AjouterLocation(self,l):
        if l in self.__LL:
            print("deja existant")
        else:
            self.__LL.append(l)
    def SupprimerLocation(self,l):
        if l in self.__LL:
            self.__LL.remove(l)
        else:
            print("ne se trouve pas")
    def FiltrerLocationDate(self,d):
        ld=[]
        for i in self.__LL:
            if i.dl==d:
                ld.append(i)
            else:
                print("n'est pas existe ")








    


        























        
