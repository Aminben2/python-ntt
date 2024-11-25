##EFM-DEV-V2-2023##
#Partie I
#Exercice 1:
def PrefixeADN(ch):
    ADN="ACGT"
    for i in ch:
        if i not in ADN:
            return False
    return  True
print(PrefixeADN("AMOG"))

#Exercice 2:
def facto(N):
    if N == 0:
        return 1
    return N * facto(N - 1)

def SuiteVn(N):
    if N == 1:
        return 1
    return (1/2 * facto(N)) + (3 * SuiteVn(N - 1)) - SuiteVn(N - 2)

def Dessiner(N):
    for i in range(N, 0, -1):
        print(" " * (N - i), end="")
        for j in range(i, 0, -1):
            print(f"V{j} ", end="")
        print()

#Partie II
#Exercice 1:
def Ordre(ch):
    lower=""
    upper=""
    nbre=""
    sym=""
    for i in ch:
        if i.isupper():
            upper+=i
        elif i.islower():
            lower+=i
        elif i.isdigit():
            nbre+=i
        else :
            sym+=i
    l=[lower,upper,nbre,sym]
    Nchaine=""
    for k in l:
        Nchaine+=k
    return Nchaine
print(Ordre("656fqsJHJH{@:"))

#Exercice 3: Dictionnaire
def RemplirRendezvous(d):
    nbRdz = int(input("Entrez le nombre de rendez-vous : "))
    
    for i in range(nbRdz):
        NumRdz = int(input("Entrez le numéro de rendez-vous : "))
        nom = input("Entrez le nom du patient : ")
        daterdz = input("Entrez la date du rdv (format JJ/MM/AAAA) : ")
        types = input("Entrez le type de rdv : ")
        prix = float(input("Entrez le prix : ")) 
        d[NumRdz].update({
            "nom_patient": nom,
            "daterdz": daterdz,
            "type": types,
            "prix": prix
        })
#2
def afficher_Rdz(rdz):
    for i, j in rdz.items():
        print(f"Les informations du rendez-vous {i} :")
        for k, l in j.items():
            print(f"{k} => {l}")

#3
def modifier_Rdz(Rdz,num):
    if num in Rdz:
        d[num]["nom_patient"]=input("Entrez le nom patient :")
        d[num]["daterdz"]=input("Entrez la date du patient :")
        d[num]["type"]=input("Entrez le type:")
        d[num]["prix"]=float(input("Entrez le prix :"))
        print("La modification à effectuée ")
    else :
        print("Le numéro n'existe pas")
#4
def supprimer_Rdz(Rdz,num):
    if num in Rdz:
        Rdz.pop(num)
        print("Suppression effectuée")
    else:
        print("Le numéro n'existe pas")
#5
def Statistiques(Rdz):
    dt={}
    with open("stats.txt", "w") as f :
        for i,j in Rdz.items():
            dt[j]['type']=dt.get(j['type'],0)+1]
        for i,j in dt.items():
            f.write(f"{i}=>{j}\n")
rdz={}
#6
choix=input("""-----------------------MENU-------------------
1-Afficher RendezVs
2-Modifier RendezVs
3-Supprimer RendezVs
4-Enregistrer les statistiques dans un fichier
5-Quitter
Entrez votre choix:""")
while True:
    if choix=="1":
        afficher_Rdz(RemplirRendezvous(rdz))
    elif choix=="2":
        num=int(input("Entrez un num de rdz vs :"))
        modifier_Rdz(rdz,num)
    elif choix=="3":
        num=int(input("Entrez un num de rdz vs :"))
        supprimer_Rdz(rdz,num)
    elif choix=="4":
        Statistiques(rdz)
    elif choix=="5":
        print("Fin")
        break
    else:
        print("Choix Invalide")
        
    
        
        
        
        


    
    
    














        

