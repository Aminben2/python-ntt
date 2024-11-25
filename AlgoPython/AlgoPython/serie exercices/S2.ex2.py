n = int(input("Entrer un nombre: "))
somme = 0
for i in range(1, n):
    if n % i == 0:
        somme += i
if somme == n:
    print(f"{n} est un nombre parfait")
else:
    print(f"{n} n'est pas un nombre parfait")
