def date_verification(j,m,a):
    if (j < 1 or j > 31) or (m<1 or m>12) or (a < 0) or (m == 2 and j>28 and not((a % 4 == 0 and a % 100 != 0) or (m == 2 and j>29 and (a % 4 == 0 and a % 100 != 0)) or (a % 400 == 0))) or (m == 4 or m == 6 or m == 9 or m == 11 and j>30):
        return "Date invalide"
    else:
        return "Date Correct"


"""
fonction date_verification(j,m,a: entier): chaine

    si (j < 1 or j > 31) or (m<1 or m>12) or (a < 0) or (m = 2 and j>28 and not((a % 4 = 0 and a % 100 <> 0) or (m = 2 and j>29 and (a % 4 = 0 and a % 100 <> 0)) or (a % 400 = 0))) or (m = 4 or m = 6 or m = 9 or m = 11 and j>30):
        retourne "Date invalide"
    sinon:
        retourne "Date Correct"

algorithme
variable j,m,a: entier
debut
    ecrire("la date (jj mm aa)")
    lire(j,m,a)

    ecrire(date_verification(j,m,a)
"""    

