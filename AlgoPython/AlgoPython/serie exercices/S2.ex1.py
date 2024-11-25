Nb = int(input("Entrez une nombre: "))
Premier = True
for i in range(2, (Nb//2)):
    if (Nb % i == 0):
        Premier = False
        break
if Premier == True:
    print(f"{Nb} Est Un Nombre Premier")
else:
    print(f"{Nb} N'est Un Nombre Premier")
