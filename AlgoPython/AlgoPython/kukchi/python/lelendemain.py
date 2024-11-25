j, m, a = int(input('Donner le jour: ')), int(input('Donner le mois: ')), int(input('Donner l\'année: '))

print(f'la date saisie: {j}/{m}/{a}')

if (j < 1 or j > 31) or (m<1 or m>12) or (a < 0) or (m == 2 and j>28 and not((year % 4 == 0 and year % 100 != 0) or (m == 2 and j>29 and (year % 4 == 0 and year % 100 != 0)) or (year % 400 == 0))) or (m == 4 or m == 6 or m == 9 or m == 11 and j>30):
    print("Date invalide")
else:
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        nbr_j = 31 #test sur les mois (31)

    elif m == 4 or m == 6 or m == 9 or m == 11 :
        nbr_j = 30 #test sur les mois (30)

    elif m == 2 and j>28 and not((year % 4 == 0 and year % 100 != 0)):
        nbr_j = 28 #test sur fevrier non bissextile
    elif m == 2 and j>29 and ((year % 4 == 0 and year % 100 != 0)):
        nbr_j = 29 #test sur fevrier non bissextile

    if j < nbr_j: #si ce n'est pas la fin du mois
        j += 1
    else: #si c'est la fin du mois
        j = 1
        if m < 12:
            m += 1
        else:
            m = 1
            a += 1

    print(f'lelendemain est: {j}/{m}/{a}')
