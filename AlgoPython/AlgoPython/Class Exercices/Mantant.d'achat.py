M_A = float(input("Entrer le montant d'achat: "))
if M_A >= 5000:
    print(f"Leur montant avec remise est: {M_A - ((M_A*20)/100)}")
elif M_A <= 5000 and M_A >= 3000:
    print(f"Leur montant avec remise est: {M_A -((M_A*15)/100)}")
elif M_A <= 3000 and M_A >=1000:
    print(f"Leur montant avec remise est: {M_A - ((M_A*10)/100)}")
else:
    print("Aucune réduction pour un montant d'achat inférieur de 1000Dh")