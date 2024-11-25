from datetime import date, time


class Patient:
    auto = 0

    def __init__(self,  n="nom", p="pre", d=date(2018, 5, 10), ad="sgfi"):
        self.__CodeP = Patient.auto
        Patient.auto += 1
        self.__Nom = n
        self.__Prenom = p
        self.__date = d
        self.__Addrese = ad

    @property
    def Nom(self):
        return self.__Nom

    @Nom.setter
    def Nom(self, n):
        self.__Nom = n

    @property
    def Prenom(self):
        return self.__Prenom

    @Prenom.setter
    def Prenom(self, n):
        self.__Prenom = n

    @property
    def code(self):
        return self.__CodeP

    @code.setter
    def code(self, n):
        self.__CodeP = n

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, n):
        self.__date = n

    @property
    def addrese(self):
        return self.__Addrese

    @addrese.setter
    def addrese(self, n):
        self.__Addrese = n

    def __str__(self):
        return f"Nom: {self.__Nom}, Prenom: {self.__Prenom}, Code Patient: {self.__CodeP}, Addresse: {self.__Addrese}, Date: {self.__date}"


class Visites:
    def __init__(self, dv=date(2018, 5, 10), hv=time(16, 25, 25), cp=0, mnt=6465):
        self.__DateVis = dv
        self.__HeureVis = hv
        self.__CodeP = cp
        self.__MntPay = mnt

    @property
    def DateVis(self):
        return self.__DateVis

    @DateVis.setter
    def DateVis(self, n):
        self.__DateVis = n

    @property
    def HeureVis(self):
        return self.__HeureVis

    @HeureVis.setter
    def HeureVis(self, n):
        self.__HeureVis = n

    @property
    def CodeClt(self):
        return self.__CodeP

    @CodeClt.setter
    def code(self, n):
        self.__CodeP = n

    @property
    def MntPay(self):
        return self.__MntPay

    @MntPay.setter
    def MntPay(self, n):
        self.__MntPay = n

    @property
    def date(self):
        return self.__DateVis

    @date.setter
    def date(self, n):
        self.__DateVis = n

    def __str__(self):
        return f"Date Visite: {self.__DateVis}, Heure visite: {self.__HeureVis}, Code Patient: {self.__CodeP}, Mantant: {self.__MntPay}"


class RendezVous:
    def __init__(self, d=date(208, 5, 10), h=time(15, 45, 12), c=0, ob="obs"):
        self.__DateRDV = d
        self.__HeureRDV = h
        self.__CodeP = c
        self.__Observation = ob

    @property
    def DateRDV(self):
        return self.__DateRDV

    @DateRDV.setter
    def DateRDV(self, n):
        self.__DateRDV = n

    @property
    def HeureRDV(self):
        return self.__HeureRDV

    @HeureRDV.setter
    def HeureVis(self, n):
        self.__HeureRDV = n

    @property
    def Code(self):
        return self.__CodeP

    @Code.setter
    def Code(self, n):
        self.__CodeP = n

    @property
    def Observation(self):
        return self.__Observation

    @Observation.setter
    def Observation(self, n):
        self.__Observation = n

    def __str__(self):
        return f"Date RDV: {self.__DateRDV}, Heure RDV: {self.__HeureRDV}, Code Patient: {self.__CodeP}, Observation: {self.__Observation}"


class CabinetMedical:
    def __init__(self, lp=[], lv=[], lr=[]):
        self.__listPatient = lp
        self.__listVisite = lv
        self.__listRDV = lr

    @property
    def listPatient(self):
        return self.__listPatient

    @listPatient.setter
    def listPatient(self, n):
        self.__listPatient = n

    @property
    def listVisite(self):
        return self.__listVisite

    @listVisite.setter
    def listVisite(self, n):
        self.__listVisite = n

    @property
    def listRDV(self):
        return self.__listRDV

    @listRDV.setter
    def Observation(self, n):
        self.__listRDV = n

    def AjouterPatient(self, p):
        if p in self.__listPatient:
            print("Patient existe deje")
        else:
            self.__listPatient.append(p)

    def Ajouter(self):
        c = int(input('Entrez le code du patient: '))
        for i in self.__listPatient:
            if i.CodeP == c:
                print('Patient existe deja')
                break
        else:
            n = input("Entrez le nom du patient")
            p = input("Entrez le prenom du patient")
            dn = date(int(input("Année")), int(
                input("Mois")), int(input("Jour")))
            ad = input("Entrez l'addrese: ")
            p = Patient(n, p, dn, ad)
            self.__listPatient.append(p)

    def PatientExistant(self, n, p):
        for i in self.__listPatient:
            if i.Nom == n and i.Prenom == p:
                return i.CodeP
            else:
                return -1

    def AjouterRDV(self, R):
        if R in self.__listPatient:
            print("Rendez vous deja existant")
        else:
            self.__listPatient.append(R)

    def RDVduJour(self, d):
        existe = False
        for i in self.__listRDV:
            if i.__DateRDV == d:
                existe = True
                print(i)
        if existe == False:
            print('Aucun rendez vous dans cette jour')

    def patientAyantDesVisites(self):
        ds = date(2022, 7, 8) - date(2022, 7, 1)
        for i in self.__listVisite:
            if (date.today() - i.__DateVis <= ds) and (date.today() > i.__DateVis):
                for j in self.__listPatient:
                    if i.CodeClt == j.CodeClt:
                        print(
                            f"Code Patient: {i.CodeClt}, Nom: {j.Nom}, Prenom: {j.Prenom}")

    def supprimerPatient(self, P):
        CP = P.CodeP
        if P in self.listPatient:
            self.__listPatient.remove(P)

            for i in self.__listVisite:
                if CP == i.CodeP:
                    self.__listVisite.remove(i)

            for i in self.__listRDV:
                if CP == i.CodeP:
                    self.__listRDV.remove(i)
            print("Suppression Avec Succes")
        else:
            print("Ce patient n'existe pas")

    def annulerRDV(self, Rdv):
        if Rdv in self.__listRDV:
            self.__listRDV.remove(Rdv)
        else:
            print("Rendez vous n'existe pas")

    def annulerRDVByDate(self, dr, hr):
        for i in self.__listRDV:
            if i.__DateRDV == dr and i.__HeureRDV == hr:
                self.__listRDV.remove(i)
                break
            else:
                print("Se RDV N'existe Pas")
