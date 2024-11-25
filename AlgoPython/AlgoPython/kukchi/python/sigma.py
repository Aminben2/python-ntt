n = int(input("entrer le nombre d'iteration: "))
x = float(input("entrer la valeur de X: "))
sigma = 0
for i in range(1,n+1):
	sigma += (x)**i
print("la somme est ", sigma)

