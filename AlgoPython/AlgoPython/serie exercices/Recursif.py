# Example 1:
"""
def factoriel(n):
    if n == 0:
        return 1
    else:
        return n*factoriel(n-1)


N = int(input("Entrez un nombre: "))
print(f"Le factoriel égale: {factoriel(N)}")
"""
# Example 2:


def suite(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2*(suite(n-1)+suite(n-2))


Nb = int(input("Entrez un nombre: "))
for i in range(1, Nb+1):
    var = suite(i)
    s =
