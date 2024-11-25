from tkinter import messagebox
from datetime import date


def openhome():
    pass


lstU = []
# -------- Parties Voitures (3 classes) ------- #


class Voiture:
    def __init__(self, im=54, mq="kd", c="fk", m=2000, p=12):
        self.__Immatriculation = im
        self.__Marque = mq
        self.__Carburant = c
        self.__Modele = m
        self.__PuissanceF = p

    @property
    def Immatriculation(self):
        return self.__Immatriculation

    @Immatriculation.setter
    def Immatriculation(self, h):
        self.__Immatriculation = h

    @property
    def Marque(self):
        return self.__Marque

    @Marque.setter
    def Marque(self, h):
        self.__Marque = h

    @property
    def Carburant(self):
        return self.__Carburant

    @Carburant.setter
    def Carburant(self, h):
        self.__Carburant = h

    @property
    def Modele(self):
        return self.__Modele

    @Modele.setter
    def Modele(self, h):
        self.__Modele = h

    @property
    def PuissanceF(self):
        return self.__PuissanceF

    @PuissanceF.setter
    def PuissanceF(self, h):
        self.__PuissanceF = h

    def __str__(self):
        return f"Immatriculation: {self.Immatriculation}, Marque: {self.Marque}, Carburant: {self.Carburant}, Modele: {self.Modele}, Puissance Fascale: {self.PuissanceF}"


class VoitureVIP(Voiture):
    def __init__(self, im=54, mq="kd", c="fk", m=2000, p=12, t="type"):
        super().__init__(im, mq, c, m, p)
        self.__Type = t

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, t):
        self.__Type = t

    def __str__(self):
        return f"{super().__str__()}, Type: {self.Type}"


class VoitureCitadine(Voiture):
    def __init__(self, im=54, mq="kd", c="fk", m=2000, p=12, g="gamme"):
        super().__init__(im, mq, c, m, p)
        self.__Gamme = g

    @property
    def Gamme(self):
        return self.__Gamme

    @Gamme.setter
    def Game(self, t):
        self.__Gamme = t

    def __str__(self):
        return f"{super().__str__()}, Type: {self.Gamme}"


class ListeVoiture:
    def __init__(self, l=[]):
        self.__listvoitures = l

    @property
    def lstVoitures(self):
        return self.__lstVoitures

    @lstVoitures.setter
    def lstVoitures(self, h):
        self.__lstVoitures = h

    def Ajouter(self, voiture):
        if voiture in self.listClient:
            messagebox.showerror('Invalide', 'Ce voiture existe déja')
        else:
            self.listClient.append(voiture)
            messagebox.showinfo('Succes', 'Le voiture est ajouté')

    def supprimer(self, imm):
        for i in self.lstVoitures:
            if i.Immatriculation == imm:
                return False
            else:
                return True

    def modifier(self, voiture, newCar):
        for i in self.lstVoitures:
            if i == voiture:
                voiture = newCar


# ------- Partie Personne (3 class) --------


class Personne:
    def __init__(self, c="l545454", p="moad", n="boujamaa"):
        self.__CiN = c
        self.__Prenom = p
        self.__Nom = n

    @property
    def Cin(self):
        return self.__CiN

    @Cin.setter
    def Cin(self, h):
        self.__CiN = h

    @property
    def Nom(self):
        return self.__Nom

    @Nom.setter
    def Nom(self, h):
        self.__Nom = h

    @property
    def Prenom(self):
        return self.__Prenom

    @Prenom.setter
    def Prenom(self, h):
        self.__Prenom = h

    def __str__(self):
        return f"Nom & Prenom: {self.Prenom} {self.Nom}, CIN: {self.Cin}"


class Client(Personne):
    def __init__(self, c="l545454", p="moad", n="boujamaa", np=54, t=63257):
        super().__init__(c, p, n)
        self.__NumPermis = np
        self.__tele = t

    @property
    def NumPermis(self):
        return self.__NumPermis

    @NumPermis.setter
    def NumPermis(self, h):
        self.__NumPermis = h

    @property
    def Tele(self):
        return self.__tele

    @Tele.setter
    def Tele(self, h):
        self.__tele = h

    def __str__(self):
        return f"{super().__str__()}, Numero Permis: {self.NumPermis}, Telephone: {self.Tele}"


class ListeClient:
    def __init__(self, lc=[]):
        self.__listClient = lc

    @property
    def listClient(self):
        return self.__listClient

    @listClient.setter
    def listClient(self, h):
        self.__listClient = h

    def Ajouter(self, client):
        if client in self.listClient:
            messagebox.showerror('Invalide', 'Ce client existe déja')
        else:
            self.listClient.append(client)
            messagebox.showinfo('Succes', 'Le client est ajouté')

    def Supprimer(self, cin):
        for i in self.listClient:
            if cin == i.Cin:
                True
            else:
                False


class Utilisateur(Personne):
    def __init__(self, c="l545454", p="moad", n="boujamaa", l="login", pwd="pwd", m="mail"):
        super().__init__(c, p, n)
        self.__Login = l
        self.__Password = pwd
        self.__Email = m

    @property
    def Login(self):
        return self.__Login

    @Login.setter
    def Login(self, h):
        self.__Login = h

    @property
    def Password(self):
        return self.__Password

    @Password.setter
    def Password(self, h):
        self.__Password = h

    @property
    def Email(self):
        return self.__Email

    @Email.setter
    def Email(self, h):
        self.__Email = h

    def __str__(self):
        return f"{super().__str__()}, Login: {self.Login}, Password: {self.Password}, Email: {self.Email}"


class ListeUtilisateur:
    def __init__(self, lu=[]):
        self.__listUtilisteur = lu

    def getlistUtilisateur(self):
        return self.__listUtilisteur

    def setlistUtilisateur(self, h):
        self.__listUtilisteur = h

    def Authentifier(self, log, pwd):
        for i in self.listUtilisateur:
            if i.Login == log and pwd == i.Password:
                openhome()
            else:
                messagebox.showerror('Invalid', 'Invalid Information')

    def Ajouter(self, utilisateur):
        if utilisateur in lstU:
            messagebox.showwarning('Invalide', 'Ce utilisateur existe déja')
        else:
            self.getlistUtilisateur.append(utilisateur)
            messagebox.showinfo(
                'Succes', 'Nouvelle utilisateur a été ajouter')

    def Supprimer(self, login):
        for i in self.listUtilisateur:
            if login == i.Login:
                True
            else:
                False


# ------ Class Location ------ #
class Location:
    id = 1

    def __init__(self, d=date(2000, 1, 1), dl=2, p=2000, c=Client(), v=Voiture()):
        self.__idLocation = Location.id
        Location.id += 1
        self.__dateLocation = d
        self.__dureeLocation = dl
        self.__Prix = p
        self.__Client = c
        self.__Voiture = v

    @property
    def idLocation(self):
        return self.__idLocation

    @property
    def dateLocation(self):
        return self.__dateLocation

    @dateLocation.setter
    def dateLocation(self, h):
        self.__dateLocation = h

    @property
    def dureeLocation(self):
        return self.__dureeLocation

    @dureeLocation.setter
    def dureeLocation(self, h):
        self.__dureeLocation = h

    @property
    def Prix(self):
        return self.__Prix

    @Prix.setter
    def Prix(self, h):
        self.__Prix = h

    @property
    def Client(self):
        return self.__Client

    @Client.setter
    def Client(self, h):
        self.__Client = h

    @property
    def Voiture(self):
        return self.__Voiture

    @Voiture.setter
    def Voiture(self, h):
        self.__Voiture = h

    def __str__(self):
        return f"Id: {self.idLocation}, Date: {self.dateLocation}, Durée: {self.dureeLocation}, Prix: {self.Prix}, Client => {self.Client}, Voiture => {self.Voiture}"


class listLocation:
    def __init__(self, ll=[Utilisateur("f6565", 'Moad', 'Boujamaa', 'Moad', '1234', 'moad@mail.com')]):
        self.__listLocation = ll

    @property
    def listLocation(self):
        return self.__listLocation

    @listLocation.setter
    def listLocation(self, h):
        self.__listLocation = h

    def AfficherListLocation(self):
        for i in self.listLocation:
            print(i)

    def AfficherListLocationVip(self):
        for i in self.listLocation:
            if isinstance(i.Voiture, VoitureVIP):
                print(i)

    def AfficherListLocationCitadine(self):
        for i in self.listLocation:
            if isinstance(i.Voiture, VoitureCitadine):
                print(i)

    def AfficherLocationMarque(self, marque):
        for i in self.listLocation:
            if i.Voiture.Marque == marque:
                print(i)

    def AfficherLocationImma(self, imma):
        for i in self.listLocation:
            if i.Voiture.Immatriculation == imma:
                print(i)

    def AfficherLocationClientCIN(self, cin):
        for i in self.listLocation:
            if i.Client.Cin == cin:
                print(i)

    def AjouterLocation(self, location):
        if location not in self.listLocation:
            self.listLocation.append(location)

    def SuppirmerLocation(self, location):
        if location in self.listLocation:
            self.listLocation.remove(location)

    def FiltrerLocationDate(self, date):
        for i in self.listLocation:
            if i.dateLocation == date:
                print(i)
