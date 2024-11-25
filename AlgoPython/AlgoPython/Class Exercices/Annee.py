print("Entrez le premier date:")
j,m,a = int(input("Entrez le jour: ")), int(input("Entrez le mois: ")), int(input("Entrez l'année: "))
print("Entrez le deuxiéme date:")
J,M,A = int(input("Entrez le jour: ")), int(input("Entrez le mois: ")), int(input("Entrez l'année: "))
if (j<=0 or j>31) or (J<=0 or J>31) or (m<=0 or m>12) or (M<=0 or M>12):
	print("La date invalide")
elif a > A or (a == A and m > M) or (a == A and m == M and j > J):
    print("Le premier date est plus grand")
else:
    print("Le deuxieme date est plus grand")