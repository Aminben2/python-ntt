from tkinter import *
from tkinter import messagebox, ttk
from tkinter.font import Font
from datetime import date


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
        self.listvoitures = l

    @property
    def lstVoitures(self):
        return self.lstVoitures

    @lstVoitures.setter
    def lstVoitures(self, h):
        self.lstVoitures = h

    def Ajouter(self, voiture):
        if voiture in self.lstVoitures:
            messagebox.showerror('Invalide', 'Ce voiture existe déja')
        else:
            self.lstVoitures.append(voiture)
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
        self.listClient = lc

    @property
    def listClient(self):
        return self.listClient

    @listClient.setter
    def listClient(self, h):
        self.listClient = h

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
        self.listUtilisateur = lu

    @property
    def listUtilisateur(self):
        return self.listUtilisateur

    @listUtilisateur.setter
    def listUtilisateur(self, h):
        self.listUtilisateur = h

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
            self.listUtilisateur.append(utilisateur)
            messagebox.showinfo(
                'Succes', 'Nouvelle utilisateur a été ajouter')

    def Supprimer(self, login):
        delete = False
        for i in self.listUtilisateur:
            if login == i.Login:
                self.listUtilisateur.remove(i)
                delete = True

        if delete == False:
            messagebox.showwarning('info', 'Ce n\'existe pas')


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


# ---------- Partie Tkinter ---------- #

root = Tk()
root.title('Agence de Location')
root.geometry('600x500')
root.configure(bg="#fff")
root.resizable(False, True)

PoppinsBig = Font(
    family='poppins',
    size=27,
    weight='bold'
)
PoppinsNormal = Font(
    family='poppins',
    size=17,
    weight='normal'
)
PoppinsSmall = Font(
    family='poppins',
    size=11,
    weight='bold'
)


def openhome():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Page d\'Accueil', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=110, y=40)

    Utilisateur = ["Ajouter Utilisateur", "Afficher Utilisateur"]
    client = ["Ajouter Client", "Afficher Client"]
    Voiture = ["Ajouter VoitureVip",
               "Ajouter VoitureCitadinne", "Afficher Voiture"]
    Location = ["Ajouter Location", "Afficher Location"]

    # Gestion Utilisateur
    def userChoix():
        if clickedUtilisateur.get() == "Ajouter Utilisateur":
            AddUser()
        else:
            showUsers()

    clickedUtilisateur = StringVar()
    clickedUtilisateur.set(Utilisateur[0])

    dropUtilisateur = OptionMenu(root, clickedUtilisateur, *Utilisateur)
    dropUtilisateur.configure(
        border=0, font=PoppinsSmall, width=15, bg='#ff9f7c', fg='#fff', pady=10)
    dropUtilisateur.place(x=85, y=130)

    btnUti = Button(root, text="Choisir", font=PoppinsSmall, border=0, fg="white", bg='#f44000', padx=5, cursor='hand2',
                    command=userChoix).place(x=145, y=200)

    # Gestion Client
    def cltChoix():
        if clickedClient.get() == "Ajouter Client":
            addClient()
        else:
            showClients()

    clickedClient = StringVar()
    clickedClient.set(client[0])

    dropClient = OptionMenu(root, clickedClient, *client)
    dropClient.configure(border=0, font=PoppinsSmall,
                         bg='#ff9f7c', fg='#fff', pady=10, width=15)
    dropClient.place(x=315, y=130)

    btnClt = Button(root, text="Choisir", font=PoppinsSmall, border=0,
                    fg="white", bg='#f44000', cursor='hand2', padx=5, command=cltChoix).place(x=380, y=200)

    # Gestion Voiture
    def CarChoix():
        if clickedCar.get() == "Ajouter VoitureVip":
            addVoitureVip()
        elif clickedCar.get() == "Ajouter VoitureCitadinne":
            addVoitureCitadinne()
        else:
            showVoitures()

    clickedCar = StringVar()
    clickedCar.set(Voiture[0])

    dropCar = OptionMenu(root, clickedCar, *Voiture)
    dropCar.configure(border=0, font=PoppinsSmall,
                      bg='#ff9f7c', fg='#fff', pady=10, width=15)
    dropCar.place(x=85, y=290)

    btnCar = Button(root, text="Choisir", font=PoppinsSmall, border=0,
                    fg="white", bg='#f44000', cursor='hand2', padx=5, command=CarChoix).place(x=145, y=355)

    # Gestion Location
    def LocationChoix():
        if clickedLocation.get() == "Ajouter Location":
            addLocation()
        else:
            showLocations()

    clickedLocation = StringVar()
    clickedLocation.set(Location[0])

    dropLocation = OptionMenu(root, clickedLocation, *Location)
    dropLocation.configure(border=0, font=PoppinsSmall,
                           bg='#ff9f7c', fg='#fff', pady=10, width=15)
    dropLocation.place(x=315, y=290)

    btnLoc = Button(root, text="Choisir", font=PoppinsSmall, border=0,
                    fg="white", bg='#f44000', cursor='hand2', padx=5, command=LocationChoix).place(x=380, y=355)


admin = Utilisateur("L154552", "Moad", "Boujamaa",
                    "Moad", "1234", "moad@2003")
lstU = [admin]

clt = Client("l4545", "Moad", "Boujamaa", 51, 6548)
lstC = [clt]

vv = VoitureVIP(54545, "BMW", "ldld", 2019, 600, "4*4")
vc = VoitureCitadine(54545, "BMW", "ldld", 2019, 600, "A")
lstV = [vv, vc]


def SignIn():
    frame = Frame(root, width=500, height=500, bg='#fff', padx=50)
    frame.place(x=50, y=0)

    title = Label(frame, text='Authentification', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=35, y=45)

    # Username part

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, ' Username')

    user = Entry(frame, fg='black', bg='#ff9f7c', width=25,
                 font=PoppinsNormal, border=0, text='username')
    user.place(x=25, y=155)
    Frame(frame, width=352, height=2, bg='black').place(x=25, y=195)
    user.insert(0, ' Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    # Password Part

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, ' Password')

    code = Entry(frame, fg='black', bg='#ff9f7c', width=25,
                 font=PoppinsNormal, border=0)
    code.place(x=25, y=255)
    Frame(frame, width=352, height=2, bg='black').place(x=25, y=295)
    code.insert(0, ' Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    def Authentifier():
        username = user.get()
        password = code.get()
        ListeUtilisateur(lstU).Authentifier(username, password)

    # Submit Button
    submit = Button(frame, text='Se Connecter', width=20, height=1,
                    font=PoppinsSmall, command=openhome, border=0, bg='#f44000', fg='#fff', cursor='hand2')
    submit.place(x=100, y=355)


def AddUser():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Add User', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=155, y=50)

    # Username part
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, ' Nom')

    user = Entry(frame, fg='black', bg='#ff9f7c', width=16,
                 font=PoppinsNormal, border=0)
    user.place(x=0, y=135)
    Frame(frame, width=225, height=2, bg='black').place(x=0, y=176)
    user.insert(0, ' Nom')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    # Prenom part
    def on_enter(e):
        pre.delete(0, 'end')

    def on_leave(e):
        name = pre.get()
        if name == '':
            pre.insert(0, ' Prenom')

    pre = Entry(frame, fg='black', bg='#ff9f7c', width=16,
                font=PoppinsNormal, border=0)
    pre.place(x=255, y=135)
    Frame(frame, width=225, height=2, bg='black').place(x=255, y=176)
    pre.insert(0, ' prenom')
    pre.bind('<FocusIn>', on_enter)
    pre.bind('<FocusOut>', on_leave)

    # Password Part

    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        name = code.get()
        if name == '':
            code.insert(0, ' Password')

    code = Entry(frame, fg='black', bg='#ff9f7c', width=16,
                 font=PoppinsNormal, border=0)
    code.place(x=0, y=220)
    Frame(frame, width=225, height=2, bg='black').place(x=0, y=260)
    code.insert(0, ' Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    # Password Part

    def on_enter(e):
        cin.delete(0, 'end')

    def on_leave(e):
        name = cin.get()
        if name == '':
            cin.insert(0, ' CIN')

    cin = Entry(frame, fg='black', bg='#ff9f7c', width=16,
                font=PoppinsNormal, border=0)
    cin.place(x=255, y=220)
    Frame(frame, width=225, height=2, bg='black').place(x=255, y=260)
    cin.insert(0, ' CIN')
    cin.bind('<FocusIn>', on_enter)
    cin.bind('<FocusOut>', on_leave)

    # Email Part

    def on_enter(e):
        mail.delete(0, 'end')

    def on_leave(e):
        name = mail.get()
        if name == '':
            mail.insert(0, ' Email')

    mail = Entry(frame, fg='black', bg='#ff9f7c', width=16,
                 font=PoppinsNormal, border=0)
    mail.place(x=0, y=305)
    Frame(frame, width=225, height=2, bg='black').place(x=0, y=345)
    mail.insert(0, ' Email')
    mail.bind('<FocusIn>', on_enter)
    mail.bind('<FocusOut>', on_leave)

    # Login Part

    def on_enter(e):
        login.delete(0, 'end')

    def on_leave(e):
        name = login.get()
        if name == '':
            login.insert(0, ' Login')

    login = Entry(frame, fg='black', bg='#ff9f7c', width=16,
                  font=PoppinsNormal, border=0)
    login.place(x=255, y=305)
    Frame(frame, width=225, height=2, bg='black').place(x=255, y=345)
    login.insert(0, ' Login')
    login.bind('<FocusIn>', on_enter)
    login.bind('<FocusOut>', on_leave)

    def Ajouter():
        nameuser = user.get()
        codeuser = code.get()
        mailuser = mail.get()
        loginuser = login.get()
        newUser = Utilisateur("L545454", "Moad", "Boujamaa",
                              nameuser, codeuser, mailuser)
        ListeUtilisateur(lstU).Ajouter(newUser)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)

    nameuser = user.get()
    codeuser = code.get()
    mailuser = mail.get()
    newUser = Utilisateur("L545454", "Moad", "Boujamaa",
                          nameuser, codeuser, mailuser)
    # Submit Button
    submit = Button(frame, text='Ajouter', width=20, height=1,
                    font=PoppinsSmall, command=Ajouter, border=0, bg='#f44000', fg='#fff', cursor='hand2')
    submit.place(x=150, y=380)


def showUsers():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Afficher Utilisateur', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=60, y=50)

    home = Button(frame, text='<- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)

    userTable = ttk.Treeview(frame)

    userTable['columns'] = ('CIN', 'Nom', 'Prenom', 'Login', 'Pwd', 'Mail')

    userTable.column('#0', anchor=W, width=70)
    userTable.column('CIN', anchor=W, width=70)
    userTable.column('Nom', anchor=W, width=70)
    userTable.column('Prenom', anchor=W, width=70)
    userTable.column('Login', anchor=W, width=70)
    userTable.column('Pwd', anchor=CENTER, width=70)
    userTable.column('Mail', anchor=W, width=70)

    userTable.heading("#0", text='Label', anchor=W)
    userTable.heading("CIN", text='CIN', anchor=W)
    userTable.heading("Nom", text='Nom', anchor=W)
    userTable.heading("Prenom", text='Prenom', anchor=W)
    userTable.heading("Login", text='Login', anchor=W)
    userTable.heading("Pwd", text='Pwd', anchor=CENTER)
    userTable.heading("Mail", text='Mail', anchor=W)

    for i in ListeUtilisateur(lstU).listUtilisateur:
        userTable.insert(parent='', index='end', iid=0, text='Parent', values=(
            i.Cin, i.Nom, i.Prenom, i.Login, i.Password, i.Email))

    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0, ' Utilisateur login')

    def delUser():
        dellog = sup.get()
        ListeUtilisateur(lstU).Supprimer(dellog)
    user = Entry(frame, fg='black', bg='#ff9f7c', width=24,
                 font=PoppinsNormal, border=0)
    user.place(x=20, y=400)
    Frame(frame, width=338, height=2, bg='black').place(x=20, y=441)
    user.insert(0, ' Utilisateur login')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    sup = Button(frame, text='Supprimer', width=10, height=1,
                 font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=delUser).place(x=380, y=400)
    userTable.place(x=10, y=150)


def addClient():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Ajouter Client', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=115, y=50)

    home = Button(frame, text='<-- Accueil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)

    def Ajouter():
        cinClt = cin.get()
        nomClt = Nom.get()
        prenomClt = Pre.get()
        numClt = Num.get()
        teleClt = Tele.get()
        newClt = Client(cinClt, prenomClt, nomClt, numClt, teleClt)
        ListeClient(lstC).Ajouter(newClt)

    def on_enter(e):
        cin.delete(0, 'end')

    def on_leave(e):
        Cin = cin.get()
        if Cin == '':
            cin.insert(0, ' CIN')

    cin = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    cin.place(x=0, y=135)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=176)
    cin.insert(0, ' CIN')
    cin.bind('<FocusIn>', on_enter)
    cin.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Nom.delete(0, 'end')

    def on_leave(e):
        nom = Nom.get()
        if nom == '':
            Nom.insert(0, ' Nom')

    Nom = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    Nom.place(x=255, y=135)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=176)
    Nom.insert(0, ' Nom')
    Nom.bind('<FocusIn>', on_enter)
    Nom.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Pre.delete(0, 'end')

    def on_leave(e):
        pre = Pre.get()
        if pre == '':
            Pre.insert(0, ' Prenom')

    Pre = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    Pre.place(x=0, y=215)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=257)
    Pre.insert(0, ' Prenom')
    Pre.bind('<FocusIn>', on_enter)
    Pre.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Num.delete(0, 'end')

    def on_leave(e):
        num = Num.get()
        if num == '':
            Num.insert(0, ' Numero Permis')

    Num = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    Num.place(x=255, y=215)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=257)
    Num.insert(0, ' Numero Permis')
    Num.bind('<FocusIn>', on_enter)
    Num.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Tele.delete(0, 'end')

    def on_leave(e):
        tele = Tele.get()
        if tele == '':
            Tele.insert(0, ' Téléphone')

    Tele = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                 font=PoppinsNormal, border=0)
    Tele.place(x=120, y=295)
    Frame(frame, width=240, height=2, bg='black').place(x=120, y=335)
    Tele.insert(0, ' Téléphone')
    Tele.bind('<FocusIn>', on_enter)
    Tele.bind('<FocusOut>', on_leave)

    submit = Button(frame, text='Ajouter', width=20, height=1,
                    font=PoppinsSmall, command=Ajouter, border=0, bg='#f44000', fg='#fff', cursor='hand2')
    submit.place(x=150, y=380)


def showClients():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Afficher Clients', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=100, y=50)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)

    userTable = ttk.Treeview(frame)

    userTable['columns'] = ('CIN', 'Nom', 'Prenom', 'NumPermis', 'Téle')

    userTable.column('#0', anchor=W, width=60)
    userTable.column('CIN', anchor=W, width=85)
    userTable.column('Nom', anchor=W, width=85)
    userTable.column('Prenom', anchor=W, width=85)
    userTable.column('NumPermis', anchor=W, width=85)
    userTable.column('Téle', anchor=CENTER, width=85)

    userTable.heading("#0", text='Label', anchor=W)
    userTable.heading("CIN", text='CIN', anchor=W)
    userTable.heading("Nom", text='Nom', anchor=W)
    userTable.heading("Prenom", text='Prenom', anchor=W)
    userTable.heading("NumPermis", text='numPermis', anchor=W)
    userTable.heading("Téle", text='Téle', anchor=CENTER)

    index = 0
    for i in ListeClient(lstC).listClient:
        userTable.insert(parent='', index='end', iid=index, text='Parent', values=(
            i.Cin, i.Nom, i.Prenom, i.NumPermis, i.Tele))
        index += 1

    userTable.place(x=8, y=150)


def addVoitureVip():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Ajouter Voiture', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=100, y=50)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)

    def AjouterVip():
        imma = ima.get()
        marque = Mrq.get()
        carb = Carburant.get()
        puis = Puissance.get()
        modele = Modele.get()
        type = Type.get()

        vip = VoitureVIP(imma, marque, carb, modele, puis, type)
        ListeVoiture(lstV).Ajouter(vip)

    def on_enter(e):
        ima.delete(0, 'end')

    def on_leave(e):
        Ima = ima.get()
        if Ima == '':
            ima.insert(0, ' Immatriculation')

    ima = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    ima.place(x=0, y=135)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=176)
    ima.insert(0, ' Immatriculation')
    ima.bind('<FocusIn>', on_enter)
    ima.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Mrq.delete(0, 'end')

    def on_leave(e):
        mrq = Mrq.get()
        if mrq == '':
            Mrq.insert(0, ' Marque')

    Mrq = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    Mrq.place(x=255, y=135)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=176)
    Mrq.insert(0, ' Marque')
    Mrq.bind('<FocusIn>', on_enter)
    Mrq.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Carburant.delete(0, 'end')

    def on_leave(e):
        carb = Carburant.get()
        if carb == '':
            Carburant.insert(0, ' Carburant')

    Carburant = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                      font=PoppinsNormal, border=0)
    Carburant.place(x=0, y=215)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=257)
    Carburant.insert(0, ' Carburant')
    Carburant.bind('<FocusIn>', on_enter)
    Carburant.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Modele.delete(0, 'end')

    def on_leave(e):
        modele = Modele.get()
        if modele == '':
            Modele.insert(0, ' Modele')

    Modele = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                   font=PoppinsNormal, border=0)
    Modele.place(x=255, y=215)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=257)
    Modele.insert(0, ' Modele')
    Modele.bind('<FocusIn>', on_enter)
    Modele.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Puissance.delete(0, 'end')

    def on_leave(e):
        puissance = Puissance.get()
        if puissance == '':
            Puissance.insert(0, ' Puissance')

    Puissance = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                      font=PoppinsNormal, border=0)
    Puissance.place(x=0, y=295)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=335)
    Puissance.insert(0, ' Puissance')
    Puissance.bind('<FocusIn>', on_enter)
    Puissance.bind('<FocusOut>', on_leave)

    submit = Button(frame, text='Ajouter', width=20, height=1,
                    font=PoppinsSmall, command=AjouterVip, border=0, bg='#f44000', fg='#fff', cursor='hand2')
    submit.place(x=150, y=380)

    def on_enter(e):
        Type.delete(0, 'end')

    def on_leave(e):
        type = Type.get()
        if type == '':
            Type.insert(0, ' Type')

    Type = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                 font=PoppinsNormal, border=0)
    Type.place(x=255, y=295)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=335)
    Type.insert(0, ' Type')
    Type.bind('<FocusIn>', on_enter)
    Type.bind('<FocusOut>', on_leave)

    submit = Button(frame, text='Ajouter', width=20, height=1,
                    font=PoppinsSmall, command=AjouterVip, border=0, bg='#f44000', fg='#fff', cursor='hand2')
    submit.place(x=150, y=380)


def addVoitureCitadinne():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Ajouter Voiture', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=100, y=50)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)

    def Ajouter():
        imma = ima.get()
        marque = Mrq.get()
        carb = Carburant.get()
        puis = Puissance.get()
        modele = Modele.get()
        gamme = Gamme.get()

        cita = VoitureVIP(imma, marque, carb, modele, puis, gamme)
        ListeVoiture(lstV).Ajouter(cita)

    def on_enter(e):
        ima.delete(0, 'end')

    def on_leave(e):
        Ima = ima.get()
        if Ima == '':
            ima.insert(0, ' Immatriculation')

    ima = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    ima.place(x=0, y=135)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=176)
    ima.insert(0, ' Immatriculation')
    ima.bind('<FocusIn>', on_enter)
    ima.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Mrq.delete(0, 'end')

    def on_leave(e):
        mrq = Mrq.get()
        if mrq == '':
            Mrq.insert(0, ' Marque')

    Mrq = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                font=PoppinsNormal, border=0)
    Mrq.place(x=255, y=135)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=176)
    Mrq.insert(0, ' Marque')
    Mrq.bind('<FocusIn>', on_enter)
    Mrq.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Carburant.delete(0, 'end')

    def on_leave(e):
        carb = Carburant.get()
        if carb == '':
            Carburant.insert(0, ' Carburant')

    Carburant = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                      font=PoppinsNormal, border=0)
    Carburant.place(x=0, y=215)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=257)
    Carburant.insert(0, ' Carburant')
    Carburant.bind('<FocusIn>', on_enter)
    Carburant.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Modele.delete(0, 'end')

    def on_leave(e):
        modele = Modele.get()
        if modele == '':
            Modele.insert(0, ' Modele')

    Modele = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                   font=PoppinsNormal, border=0)
    Modele.place(x=255, y=215)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=257)
    Modele.insert(0, ' Modele')
    Modele.bind('<FocusIn>', on_enter)
    Modele.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Puissance.delete(0, 'end')

    def on_leave(e):
        puissance = Puissance.get()
        if puissance == '':
            Puissance.insert(0, ' Puissance')

    Puissance = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                      font=PoppinsNormal, border=0)
    Puissance.place(x=0, y=295)
    Frame(frame, width=240, height=2, bg='black').place(x=0, y=335)
    Puissance.insert(0, ' Puissance')
    Puissance.bind('<FocusIn>', on_enter)
    Puissance.bind('<FocusOut>', on_leave)

    def on_enter(e):
        Gamme.delete(0, 'end')

    def on_leave(e):
        gamme = Gamme.get()
        if gamme == '':
            Gamme.insert(0, ' Gamme')

    Gamme = Entry(frame, fg='black', bg='#ff9f7c', width=17,
                  font=PoppinsNormal, border=0)
    Gamme.place(x=255, y=295)
    Frame(frame, width=240, height=2, bg='black').place(x=255, y=335)
    Gamme.insert(0, ' Gamme')
    Gamme.bind('<FocusIn>', on_enter)
    Gamme.bind('<FocusOut>', on_leave)

    submit = Button(frame, text='Ajouter', width=20, height=1,
                    font=PoppinsSmall, command=Ajouter, border=0, bg='#f44000', fg='#fff', cursor='hand2')
    submit.place(x=150, y=380)


def showVoitures():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Afficher Voitures', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=90, y=50)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)

    userTable = ttk.Treeview(frame)

    userTable['columns'] = ('CIN', 'Nom', 'Prenom', 'NumPermis', 'Téle')

    userTable.column('#0', anchor=W, width=60)
    userTable.column('CIN', anchor=W, width=85)
    userTable.column('Nom', anchor=W, width=85)
    userTable.column('Prenom', anchor=W, width=85)
    userTable.column('NumPermis', anchor=W, width=85)
    userTable.column('Téle', anchor=CENTER, width=85)

    userTable.heading("#0", text='Label', anchor=W)
    userTable.heading("CIN", text='CIN', anchor=W)
    userTable.heading("Nom", text='Nom', anchor=W)
    userTable.heading("Prenom", text='Prenom', anchor=W)
    userTable.heading("NumPermis", text='numPermis', anchor=W)
    userTable.heading("Téle", text='Téle', anchor=CENTER)

    index = 0
    for i in ListeVoiture(lstV).lstVoitures:
        userTable.insert(parent='', index='end', iid=index, text='Parent', values=(
            i.Cin, i.Nom, i.Prenom, i.NumPermis, i.Tele))
        index += 1

    userTable.place(x=8, y=150)
    loginPage.place(x=400, y=0)


def addLocation():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Ajouter Location', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=90, y=50)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)


def showLocations():
    frame = Frame(root, width=600, height=500, bg='#fff', padx=50)
    frame.place(x=0, y=0)

    title = Label(frame, text='Afficher Locations', bg='#fff',
                  fg='black', font=PoppinsBig)
    title.place(x=80, y=50)

    home = Button(frame, text='<-- Acceuil', width=10, height=1,
                  font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=openhome)
    home.place(x=0, y=0)
    loginPage = Button(frame, text='Login -->', width=10, height=1,
                       font=PoppinsSmall, border=0, bg='#f44000', fg='#fff', cursor='hand2', command=SignIn)
    loginPage.place(x=400, y=0)


SignIn()

root.mainloop()
