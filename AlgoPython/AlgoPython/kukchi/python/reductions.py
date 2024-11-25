montant = float(input("La montant d'achat: "))

if montant > 5000:
	to_pay = montant - (montant * 20/100)
	print(f"{to_pay}Dhs à payer (20%)")

elif 3000 < montant <= 5000:
	to_pay = montant - (montant * 15/100)
	print(f"{to_pay}Dhs à payer (15%)")

elif 1000 < montant <= 3000:
	to_pay = montant - (montant * 10/100)
	print(f"{to_pay}Dhs à payer (10%)")

else:
	print(f"Aucune réduction\n{montant}Dhs à payer")


