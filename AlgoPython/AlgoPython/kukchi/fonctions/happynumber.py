def happy(nb):
	isHappy = False
	nombre = str(nb)
	stop = False
	while stop == False:
		s = 0
		# string = ''
		for i in nombre:
			s += int(i)**2
			nombre = str(s)
			print(f"{i}^2 = {int(i)**2}")
		print(f"Nouveau: {s}")

		if nombre == '1':
			isHappy = True
			break

		if int(nombre) < 10:	 
			stop = True
	return isHappy
	
n = int(input("Entrer un nombre: "))
print(f"Nombre de depart: {n}")
if happy(n) == True:
	print(f"{n} est un porte bonheur")
else:
	print(f"{n} n'est pas un porte bonheur")
