def remplissage_notes():
    notes_stagiaire = {}
    nb = int(input("Entrez le nombre des stagiaire: "))
    n = int(input("Entrer le nombre des notes: "))

    for i in range(nb):
        dictNotes = {}
        nomStg = input("Entrer le nom de stagiaire: ")
        for j in range(n):
            noteStg = float(input(f"Entrer la note de M10{j+1}: "))
            dictNotes[f'M10{j+1}'] = noteStg 
            
        notes_stagiaire.update({nomStg:dictNotes})
    return notes_stagiaire


def calcul_moyen(d):
    moyenne_stagiaire = {}
    for k,v in d.items():
        les_moyennes = sum(v.values())/len(v.keys())
        moyenne_stagiaire.update({k:les_moyennes})
    return moyenne_stagiaire


def supp_stg(stg, d):
    del d[stg]
    notes_stagiaire = d
    return notes_stagiaire

def moyenne_class(d):
    moyenne_class = sum(calcul_moyen(d).values())/len(calcul_moyen(d).keys())
    return moyenne_class
    
def sort_stagiaires(d):
    # Short way
    stgList = sorted([(k, v) for (k, v) in d.items()] )
    newDict = dict(stgList)
    return newDict

def notesUpdate(name, d):
    print(f'stagiaire : {name}')
    dic = d[name]
    for module, note in dic.items():
        notes = float(input(f'Entrer la nouvelle note de {module}: '))
        dic[module] = notes
    d[name] = dic
    notes_stagiaire = d
    return notes_stagiaire

def premiere_class(d):
    moyennes = calcul_moyen(d)
    topMoyenne = max(moyennes.values())
    stagieaires = moyennes.keys()
    for stagieaire in stagieaires:
        if moyennes[stagieaire] == topMoyenne:
            return stagieaire

def topModule(d):
    for stg, notes in d.items():
    # for module, note in notes.items():
        maxNote = max(notes.values())
        modules = notes.keys()
        for module in modules:
            if notes[module] == maxNote:
                maxModule = module
        print(f'le stagiaire {stg} a eu la note maximale {maxNote} dans le module : {maxModule}')

def moyenne_module(d):
    M01 = []
    M01_stg = {}
    for k,v in d.items():
        for ky, vl in v.items():
            if ky == 'M01':
                M01.append(vl)
                M01_stg.update({k:{ky:vl}})
    return sum(M01)/len(M01)


# notes_stagiaire =  {"stg1":{"M01" : 15, "M02": 17, "M03" : 18 } , "stg2": {"M01" : 15,
 # "M02": 17, "M03" : 10},"stg3":{"M01" : 12, "M02": 8, "M03" : 11 } }


MENU = """
-------------Menu-------------
0 : Remplir les notes
1 : Afficher les notes
2 : Afficher la moyenne de chaque stagiaire .
3 : Trier le dictionnaire des notes .
4 : Modifier les notes d’un stagiaire .
5 : Afficher le premier de la classe .
6 : Supprimer un stagiaire .
7 :Afficher la moyenne de la classe pour le premier module 
8: Quittez le programme"""


print(MENU.strip())
choice = int(input('Tapez votre choix : '))

while choice < 0 or choice > 8:
    choice = int(input('Tapez votre choix : '))
while True:
    if choice == 0:
        notes_stagiaire = remplissage_notes()

    elif choice == 1:
        for k, v in notes_stagiaire.items():
            print(f"-------------\n{k} :")
            for module, note in v.items():
                print(f"{module.capitalize()}: {note}")
    elif choice == 2:
        moyennes = calcul_moyen(notes_stagiaire)
        for k, v in moyennes.items():
            print(f"-------------\n{k.capitalize()}: {v}")

    elif choice == 3:
        notes_stagiaire = sort_stagiaires(notes_stagiaire)

    elif choice == 4:
        name = input("Entrer le nom de stagiaire : ")
        notesUpdate(name, notes_stagiaire)
    elif choice == 5:
        print(premiere_class(notes_stagiaire))
    elif choice == 6:
        stg = input("Entrer le nom de stagiaire : ")
        supp_stg(stg, notes_stagiaire)
    elif choice == 7:
        print(moyenne_class(notes_stagiaire))
    elif choice == 8:
        print("Merci!!")
        break
    else:
        choice = int(input('Tapez votre choix : '))

    continu = input('\nContinue? (y/n) ').lower()
    if continu == 'y':
        print(MENU)
        choice = int(input('Tapez votre choix : '))
    else:
        break

