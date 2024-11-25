#Exercice 5:
def facto(nb):
    if nb==0:
        return 1
    return nb*facto(nb-1)
def Suite_U(N):
    if N==0:
        return 1
    else :
        return Suite_U(N-1)*facto(N-1)
def Suite_V(N):
    suite = 0
    for i in range(1, N+1):
        suite +=Suite_U(i)/(i**N)
    return suite
n = int(input("Entrez un nombre :"))
print(Suite_V(n))
L = ['ahmed' , 'ahmedi', 'karimi', 'chihab']
print("-".join(L))
    
