def S(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return S(n-1)*S(n-2)

def calc_aff(user):
	if user > 0:
		produit = 1
		for i in range(1,user+1):
			print(f"S({i}) = {S(i)}")
			produit *= S(i)
			
		print(f"le produit est {produit}")
	else:
		print("Erreur")

user = int(input("entrer le nombre: "))
calc_aff(user)



"""
Fonction S(n: reel): reel
	si n = 1 alors
		retourne 1
	sinon
		si n = 2 alors
		retourne 2
"""






