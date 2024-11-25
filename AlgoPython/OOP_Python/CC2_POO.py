# -------- Parties Voitures (3 classes) ------- #
from tkinter.font import Font
from tkinter import messagebox
from tkinter import *
from datetime import date


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


# V1 = Voiture(656565, "Dacia", "idk", 2015, 300)
# V2 = VoitureVIP(515155, "BMW", "idk2", 2017, 500, "SUV")
# V3 = VoitureCitadine(656565, "Ford", "idk3", 2018, 500, "A")

# print(V1)
# print(V2)
# print(V3)

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


# print(Personne("L674511", "Moad", "Boujamaa"))


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


# print(Client())


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

    @property
    def listUtilisateur(self):
        return self.__listUtilisteur

    @listUtilisateur.setter
    def listUtilisateur(self, h):
        self.__listUtilisteur = h

    def Authentifier(self, log, pwd):
        for i in self.listUtilisateur:
            if i.Login == log and pwd == i.Password:
                return True
            else:
                return False

    def Ajouter(self, utilisateur):
        if utilisateur in self.listUtilisateur:
            self.listUtilisateur.Append(utilisateur)
        else:
            print("Invalid")

    def Supprimer(self, login):
        lstU = self.listUtilisateur
        for i in self.listUtilisateur:
            if login == i.Login:
                self.listUtilisateur.remove(i)
            else:
                print("Invalid")


# print(Utilisateur())

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


# c = Location(date(2020, 12, 12), 2, 600, Client('l541254', "Moad",
#              "Moad", 15, 25642), Voiture(154556, "BMW", "idk", 2015, 2032))
# print()
# print("########")
# print(Location())
# print()
# print(c)


class listLocation:
    def __init__(self, ll=[]):
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


c1 = Location(date(2020, 12, 12), 2, 600, Client('c1', "Moad",
                                                 "Moad", 15, 25642), Voiture(154556, "BMW", "idk", 2015, 2032))
c2 = Location(date(2021, 12, 13), 2, 600, Client('c2', "Moad",
                                                 "Moad", 15, 25642), VoitureCitadine(15254, "mazda", "idk2", 2020, 1254, "gamme"))
c3 = Location(date(2020, 12, 12), 2, 600, Client('c3', "Moad",
                                                 "Moad", 15, 25642), VoitureCitadine(15254, "mazda", "idk2", 2020, 1254, "gamme"))
c4 = Location(date(2020, 12, 12), 2, 600, Client('c4', "Moad",
                                                 "Moad", 15, 25642), VoitureVIP(151515, "Mercedes", "idk", 2015, 1522, "4*4"))
c5 = Location(date(2020, 12, 12), 2, 600, Client('c5', "Moad",
                                                 "Moad", 15, 25642), VoitureVIP(151515, "Mercedes", "idk", 2015, 1522, "SUV"))
c6 = Location(date(2003, 5, 11), 4, 203, Client('c6', "Moad", "Boujmaa",
              25, 65214), VoitureCitadine(514, "Dacia", "cln", 2022, 1254, "A"))
ll = [c1, c2, c3, c4, c5, c6]
# print(listLocation(ll).FiltrerLocationDate(date(2021, 12, 13)))


root = Tk()
root.title('Login')
root.geometry('600x500+300+200')
root.configure(bg="#fff")
root.resizable(False, True)
PoppinsBig = Font(
    family='poppins',
    size=30,
    weight='bold'
)
PoppinsNormal = Font(
    family='poppins',
    size=17,
    weight='normal'
)
PoppinsSmall = Font(
    family='poppins',
    size=12,
    weight='bold'
)


def SignIn():
    username = user.get()
    password = code.get()


frame = Frame(root, width=500, height=400, bg='#fff', padx=50)
frame.place(x=50, y=15)

title = Label(frame, text='Sign In', bg='#fff',
              fg='black', font=PoppinsBig)
title.place(x=145, y=35)


# Username part
def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, fg='black', bg='#ff9f7c', width=25,
             font=PoppinsNormal, border=0, text='username')
user.place(x=25, y=155)
Frame(frame, width=352, height=2, bg='black').place(x=25, y=195)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)


# Password Part
def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, fg='black', bg='#ff9f7c', width=25,
             font=PoppinsNormal, border=0)
code.place(x=25, y=255)
Frame(frame, width=352, height=2, bg='black').place(x=25, y=295)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

# Submit Button
submit = Button(frame, text='Sign In', width=20, height=1,
                font=PoppinsSmall, command=SignIn, border=0, bg='#f44000', fg='#fff', cursor='hand2')
submit.place(x=100, y=350)


root.mainloop()
