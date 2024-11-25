def factoriel(A):
    if A == 0:
        return 1
    elif A < 0:
        return None
    else:
        F = 1
        for i in range(1, A):
            F *= i
        return F


print(factoriel(150))
