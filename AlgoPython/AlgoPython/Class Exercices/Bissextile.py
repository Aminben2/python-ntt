A = int(input("Enter l'année: "))
if (A%4 == 0 and A%100 != 0) or A%400 == 0:
    print("L'année est bissextile")
else:
    print("L'année n'est pas bissextile")