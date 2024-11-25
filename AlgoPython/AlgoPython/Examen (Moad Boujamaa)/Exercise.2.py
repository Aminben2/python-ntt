# --- 1 --- #
school = {"TDI": ("TS", 1200), "TMSIR": ("T", 1300),
          "TRI": ("TS", 1100), "INFO": ("TS", 900), }

# --- 2 --- #


def ajouter(d):
    NB = int(input("Entrez le nombre des filiére pour ajouter: "))
    lst = []
    for i in range(NB):
        NomF = input("Entrez le nom de filiére: ")
        if NomF in d:
            print("Ce filiére existe déja")
        else:
            NV = input("Entrez le niveau: ")
            NH = input("Entrez le nombre d'heure: ")
            lst.append(NV)
            lst.append(NH)
            tpl = tuple(lst)
        d.update({NomF: tpl})
    print(d)


# --- 3 --- #
# def info(d):

# --- 4 --- #
def changer_heure(d):
    NomF = input("Entrez le nom de fliére: ")
    NH = int(input("Entrez le nombre des heure: "))
    value = d[NomF]
    valeur = list(value)
    del valeur[-1]
    valeur.append(NH)

# --- 5 --- #


def supprimer(d):
    NomF = input("Entrez le nom de filiére: ")
    if NomF not in d:
        print("Ce filiére n'existe pas")
    else:
        del d[NomF]
    print(d)

# --- 6 --- #
# def dict(d):


print("""
--------- Menu ---------
1- Ajouter une filiére
2- Information
3- Changer heure
4- Supprimer une filiére
5- 
""")
ch = int(input("Tapez votre choix: "))
if ch == 1:
    ajouter(school)
elif ch == 2:
    info(school)
elif ch == 3:
    changer_heure(school)
elif ch == 4:
    supprimer(school)
