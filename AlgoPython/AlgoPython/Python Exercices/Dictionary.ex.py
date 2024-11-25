# # Example:
# school_class = {}
# while True:
#     name = input("Enter the student's name (or type exit to stop): ")
#     if name == 'exit':
#         break
#     score = int(input("Enter the student's score(0-10): "))
#     if name in school_class:
#         school_class[name] += (score,)
#     else:
#         school_class[name] = (score,)
#         for name in sorted(school_class.keys()):
#             adding = 0
#             counter = 0
#         for score in school_class[name]:
#             adding += score
#             counter += 1
#             print(name, ":", adding / counter)

# Exercice 1:


# # Exercice 2:
# def etudiant(chaine):
#     d = {}
#     lignes = chaine.splitlines()
#     for i in lignes:
#         infos = i .split(";")
#         d.update({int(infos[0]): infos[1]+" "+infos[2]})
#     return d
# C = """213615200;BESNIER;JEAN
# 21356488;DUPOND;MARC
# 214665555;DURAND;JULIE"""
# print(etudiant(C))

# ------- Exercice 3 ------- #
# def totalVentes(d):  # 1
#     somme = 0
#     for i in d.values():
#         somme += i
#     return somme


# def meilleurVendeur(d):  # 2
#     for i in d:
#         if d[i] == max(d.values()):
#             m_v = i


# def suprimerPV(d):
#     for i, j in d.items():
#         if j == min(d.values()):
#             p_v = i
#     del d[p_v]


# def suprimer(nom_v, d):
#     if nom_v in d:
#         del d[nom_v]
#     else:
#         print("Ce vendeur n'existe pas: ")


# def trier(d):
#     d_trier = {}
#     for i in sorted(d.values(), reverse=True):
#         for j in d:
#             if d[j] == i:
#                 d_trier.update({j: i})
#     return d_trier


# def modifietr_vendeur(nom_v, d):
#     if nom_v in d:
#         d[nom_v] = int(input("Entrez le nouveau nombre des ventes: "))
#     else:
#         print("Ce vendeur n'existe pas")


# def enregistrer_ventes(d):
#     with open("ventes.txt", "w") as fichier:
#         for i, j in d.items():
#             fichier.write(f"{i} => {j}\n")


# ventes = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21}
# choix = 2
# while choix != 10:
#     print("""
# -------------Menu-------------
# 1 : Ajouter les ventes
# 2 : Afficher les ventes.
# 3 : Afficher les ventes triées.
# 4 : Modifier les ventes d’un vendeur .
# 5 : Rechercher les ventes d’un vendeur .
# 6 : Supprimer un vendeur .
# 7 :Afficher le nombre total des ventes
# 8 :Afficher le vendeur qui a réalisé plus de vente
# 9 : Enregistrer dans un fichier
# 10: Quittez le programme """)
#     choix = int(input("Tapez votre choix: "))
#     if choix == 1:
#         nb_ventes = int(input("Entrez le nombre des ventes a ajouter: "))
#         for i in range(nb_ventes):
#             nomv = input("Entrez le nom de vendeur: ")
#             nbv = input("Entrez le nombre des ventes: ")
#             ventes.update({nomv: nbv})
#     elif choix == 2:
#         for i, j in ventes.items():
#             print("Nom Vendeur: ", i, "Nombre Ventes", j)
#     elif choix == 3:
#         print("Les ventes triées sont comme suit: ")
#         d = trier(ventes)
#         for i, j in d.items():
#             print("Nom Vendeur: ", i, "Nombre Ventes", j)
#     elif choix == 4:
#         nom_v = input("Entrez le nom vendeur à modifier: ")
#         modifietr_vendeur(nom_v, ventes)
#     elif choix == 5:
#         nom_v = input("Entrez le nom de vendeur: ")
#         if nom_v in ventes:
#             print(f"Le vendeur {nom_v} a fait: {ventes[nom_v]} ventes")
#         else:
#             print(f"{nom_v} n'existe pas")
#     elif choix == 6:
#         nom_v = input("Entrez le nom du vendeur à suprimer")
#         suprimer(nom_v, ventes)
#     elif choix == 7:
#         print(f"Le total des ventes est: {totalVentes(ventes)}")
#     elif choix == 8:
#         print(
#             f"Le vendeur qui a realisé le max des ventes est: {meilleurVendeur(ventes)}")
#     elif choix == 9:
#         enregistrer_ventes(ventes)
#         print("Enregistré avec succes")
#     elif choix == 10:
#         print("Au revoir")
#     else:
#         print("Choix invalide")

# ---------------- Exercise 4 -----------------#
def remplir(d):
    nbs = int(input("Entrez le nombre des stagiaires: "))
    for i in range(nbs):
        # demander le clé
        codes = input("Entrez le code du stagiaire: ")
        notes = {}
        for i in range(3):
            nomm = input('Entrez le nom de stagiare: ')
            note = float(input("Entrez la note du module: "))
            notes.update({nomm: note})
        d.update({codes: notes})


def calcul_moyenne(d):
    for i, j in d.items():
        s = 0
        for k in j.values():
            s += k
        print(f"Le stagiare: {i} a eu {s / len(j)}")


def supprimer(d, noms):
    if noms in d:
        del d[noms]
    else:
        print("ce stagiaire n'existe pas")


def moyenne_classe(d):
    ms = 0
    for i, j in d.items():
        s = 0
        for k in j.values():
            s += k
            ms += s(len(j))
    print(f"La moyenne de la classe est: {ms/len(d)}")


# # -------------- EXERCISE 5 ---------------- #
# prd = {}
# nbp = int(input("Entrez le nombre des produit: "))

# for i in range(nbp):
#     # demander la clé
#     code_p = input("Entrez le code de produit: ")
#     # Delander la valeur : liste
#     l_infos = []
#     nomp = input("Entrez le nom de produit: ")
#     l_infos.append(nomp)
#     pa = input("Entrez Le prix d'achat: ")
#     l_infos.append(nomp)
#     pv = input("Entrez le peix de vente: ")
#     l_infos.append(pv)
#     qte = input("Entrez la quantité: ")
#     l_infos.append(qte)
#     prd.update({code_p: l_infos})

# def rechercher(d, cp):
#     return cp in d

# def modifier(d, cp):
#     if cp in d:
#         l_infos = []
#         nomp = input("Entrez le nom de produit: ")
#         l_infos.append(nomp)
#         pa = input("Entrez Le prix d'achat: ")
#         l_infos.append(nomp)
#         pv = input("Entrez le peix de vente: ")
#         l_infos.append(pv)
#         qte = input("Entrez la quantité: ")
#         l_infos.append(qte)
#         d[cp] = l_infos
#     else:
#         print("Ce produit n'existe pas")

# def suprimer(d):
#     exist = False
#     for i, j in d.items():
#         if j[-1] == 0:
#             i_fini = i
#             exist = True
#     if exist:
#         del d[i_fini]
#     else:
#         print("Aucun produit fini")

# def qte_total(d):
#     qtet = 0
#     for i in d.values():
#         qtet += i[-1]
#     return qtet

# def remplir():
#     d = {}
#     while True:
#         codec = input("Le code du client (Tapez zero pour arretez): ")
#         if codec == 0:
#             break
#         else:
#             # Demander la valeur
#             d_p = {}
#             nbp = input("Entrez le nombre des produits acheter: ")
#             for i in range(nbp):
#                 codep = input("Entrez le code du produit avheter: ")
#                 qtep = input("Entrez la quantité acheter: ")
#                 d_p.update({codep: qtep})
#             d.update({codec: d_p})

# def mnt_apayer(d_v, d_p):
#     for i, j in d_v.items():
#         prix = 0
#         for k, l in j.items():
#             prix += d_p[k][2]*l
#     print(f"Le client: {i} a payé: {prix}")

# def total_vente(d_v, d_p):
#     prix = 0
#     for i, j in d_v.items():
#         for k, l in j.items():
#             prix += d_p[k][2]*l
#     print(f"Le total des ventes est: {prix}")

# def enregistrer(d):
#     with open("Product.txt", "w") as f:
#         for i, j in d.items():
#             f.write(f"Codep: {i} -Nom P: {j[0]} - PA : {j[1]}")
#             f.write(f"-PV: {j[2]} -Qte: {j[3]}")
