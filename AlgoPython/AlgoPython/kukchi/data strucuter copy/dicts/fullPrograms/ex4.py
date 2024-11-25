def remplissage(d):
    n = int(input("Entrez le nombre des stagiaire a ajouté: "))
    nb = int(input("Entrer le nombre des notes: "))
    d = {}
    for i in range(n):
        nomStg = input("entrer le nom de stagiaire: ")
        d_notes = {}
        for j in range(1, nb+1):
            note = float(input(f"Entrer la note de M0{j}:"))
            d_notes[f"M0{j}"] = note
        d.update({nomStg: d_notes})
    return d


Note_stagiaire = {"stg1": {"M01": 15, "M02": 17, "M03": 18}, "stg2": {
    "M01": 15, "M02": 17, "M03": 10}, "stg3": {"M01": 12, "M02": 8, "M03": 11}}


def moyenne(d):
    les_moyennes = {}
    for i, j in d.items():
        moyennes = sum(j.values())/len(j.values())
        les_moyennes.update({i: moyennes})
    return les_moyennes


def stag(d, n):
    del d[n]
    return d


print(stag(Note_stagiaire, "stg2"))
