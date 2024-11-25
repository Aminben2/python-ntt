#Remplissage d'un dict nv0:
'''dic={}
nb=int(input("Entrez le nombre d'éléments du dict :"))
for i in range(nb):
    s=input("Entrez le nom du stagiaire :")
    moy=float(input("Entrez la moyenne :"))
    dic.update({s:moy})
print(dic)
#Remplissage d'un dict nv1:
dic1={}
nb=int(input("Entrez le nombre d'éléments du dict :"))
Nm=int(input("Entrez le nombres du module :"))
for i in range(nb):
    s=input("Entrez le nom du stagiaire :")
    moy=[]
    for j in range(Nm):
        note=float(input("Entrez la note du module :"))
        moy.append(note)
    dic1.update({s:moy})
print(dic1)
#Remplissage d'un dict nv2:
dicE={}
n=int(input("Entrez le nombre d'éléments du dict :"))
Nmod=int(input("Entrez le nombre des modules :"))
for i in range(Nmod):
    mod=input("Entrez le nom du module :")
    dicI={}
    for j in range(n):
        s=input("Entrez le nom du stagiaire :")
        note=float(input("Entrez la note :"))
        dicI.update({s:note})
    dicE.update({mod:dicI})
print(dicE)   

#1:
with open("file.txt", "r") as f:
    d={}
    for i in f:
        info=i.strip().split(";")
        location=info[0]
        nom=info[1]
        date=info[2]
        imm=info[3]
        marque=info[4]
        d[location]={"Nom_Client": nom,
                     "Date": date,
                     "immatricule": imm,
                     "marque": marque
                     }
print(d)
#2
def afficher_location(d):
    for i,j in d.items():
        print(f"Location => {i} :")
        for k,l in j.items():
            print(f"{k}=>{l}")
afficher_location(d)
#3
def modifier_location(d,num):
    if num in d:
        d[num]["Nom_client"]=input("Entrez le nom :")
        d[num]["Date"]=input("Entrez la date :")
        d[num]["immatricule"]=input("Entrez l'immatriculation :")
        d[num]["marque"]=input("Entrez la marque :")
        print("Modification efféctuée")
    else :
        print("numéro invalide")
#4
def supprimer_location(d,num):
    if num in d:
        d.pop(num)
        print("La suppression efféctuée")
    else:
        print("numéro invalide")
#5
def meilleur_voiture(d):
    cmpt_v={}
    for i,j in d.items():
        cmpt_v[imm]=cmpt_v.get(imm,0)+1
    v_max=max(cmpt_v, key=cmpt_v.get)
    return v_max
#6
while True:
    choix = input("""-----------------------MENU---------------------
1-Afficher Locations
2-Modifier Location
3-Supprimer Location
4-Afficher la voiture la plus louée
5-Quitter
Entrez votre choix : """)

    if choix == "1":
        print("Les informations de chaque location sont :", afficher_location(d))
    elif choix == "2":
        modifier_location(d, input("Entrez un numéro"))
        print("Les informations de la location ont été modifiées avec succès.")
    elif choix == "3":
        supprimer_location(d, input("Entrez un numéro"))
        print("La location a été supprimée avec succès.")
    elif choix == "4":
        print("La voiture la plus louée a l'immatriculation :", meilleur_voiture(d))
    elif choix == "5":
        print("Fin")
        break
    else:
        print("Choix invalide")

#exercice dict V2:
#1:
def RemplirRendezvous(rdz):
    nbRdz=int(input("Entrez le nombre de rdz vs :"))
    for i in range(nbRdz):
        numRdz=int(input("Entrez le numéro de rdz vs :"))
        nom=input("Entrez le nom patient :")
        date=input("Entrez la date patient :")
        type=input("Entrez le type de patient :")
        prix=float(input("Entrez le prix :")
        d.[numRdz].update({"nom_patient":nom,
                    "daterdz":date,
                    "type":type,
                    "prix":prix
                    })
#2
def afficher_Rdz(rdz):
    for i,j in rdz.items():
        print(f"Rendez-vous num° {i}")
        for k,l in j.items():
            print(f"{k} => {l}")
#3
def modifier_Rdz(rdz,num):
    if num in rdz:
        rdz[num]["nom_patient"]=input("Entrez un nom :")
        rdz[num]["daterdz"]=input("Entrez une date de rdz vs :")
        rdz[num]["type"]=input("Entrez le type de rdz vs :")
        rdz[num]["prix"]=float(input("Entrez le prix :"))
        print("Modification effectuée")
    else:
        print("Numéro invalide")
#4
def supprimer_Rdz(rdz, num):
    if num in rdz:
        del rdz[num]
        print("Suppression effectuée")
    else:
        print("Numéro invalide")
#5
def Statistiques(rdz):
    statique={}
    for i,j in rdz.items():
        statique[j['type']=statique.get(j['type'],0)+1]
    for i,j in rdz.items():
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

#Serie exercice dict
#exe01:
#b
def nb_total_ventes(d):
    return sum(d.values()) 

d={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}       
print(nb_total_ventes(d))       
#c
def max_ventes(d):
    m=max(d.values())
    for i in d:
        if d[i]==m:
            return i
print(max_ventes(d))
#d
def supprime_vendeur_min(d):
    m=min(d.values())
    l=[]
    for i in d:
        if d[i]==m:
            l.append(i)
    for i in l:
        d.pop(i)
#e
def supprime_vendeur(d,nom):
    if nom in d:
        d.pop(nom)
    else:
        print("Le nom vendeur est invalide")
#f
def trier(d):
    return sorted(d, key=d.get, reverse=True)

print(trier(d))
#g
def modifier(d,nom):
    if nom in d:
        d[nom]=int(input("Entrez le nombres des ventes:"))
    else:
        print("Nom vendeur invalide")
#h
def enregistrer(d):
    with open("ventes.txt", "w") as f:
        for i,j in d.items():
            f.write(f"{i} => {j}\n")

#exe04:
#1
def Remplir(d):
    nS=int(input("Entrez le nombres des stagiaires :"))
    nM=int(input("Entrez le nombres des modules :"))
    for i in range(nS):
        nom=input("Entrez le nom de stagiaires :")
        di={}
        for j in range(nM):
            mod=input("Entrez le nom du module :")
            note=int(input("Entrez la note de module :"))
            di.update({mod:note})
        d.update({nom:di})
            
d={}
Remplir(d)
print(d)'''
#2
def moyenne_stg(d):
    for i,j in d.items():
        moy=0
        for k,l in j.items():
            moy+=(l)/len(j)
        print("la moyenne est", moy)

#2ème methode:
def moyenne(d):
    for i,j in d.items:
       m= sum(j.values())/len(j)
       print(f"la moyenne du stagiare {i} est {m}")
      
#3
def supprimer(d,nom):
    if nom in d:
        del d[nom]
    else:
        print("Nom invalide")
#4
def moyenne_classe(d):
    s=0
    for i,j in d.items():
        m=sum(j.values())/len(j)
        s+=m
    return s/len(d)














