def U(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return 2*(U(n-1)+U(n-2))

n = int(input("Entrer un nombre: "))
somme = 0
for i in range(1,n+1):
	print(f"U({i}) = {U(i)}")
	somme += U(i)

print(f"la somme est {somme}")

# print(U(n))