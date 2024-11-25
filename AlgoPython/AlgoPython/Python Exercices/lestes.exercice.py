# Exercice 3:
L = [1, 5, 4, 6, 9]
for i in range(len(L)):
    L[i] += 1
print(L)


# Exercice 4:
Nb = int(input("Entrez le nombre le longeur de listes: "))
Pre = []
Des = []
third = []
for i in range(1, Nb+1):
    pr = int(input(f"Entrez le nombre numero {i} de liste 1: "))
    Pre.append(pr)
print()
print()
for i in range(1, Nb+1):
    ds = int(input(f"Entrez le nombre numero {i} de liste 2: "))
    Des.append(ds)
print()
print(Pre)
print(Des)

for i in range(len(Pre)):
    third.append(Pre[i]+Des[i])
print(f"L1 + L2 = {third}")


# # Exercice 5:
# L1 = []
# N = int(input("Enter le nombre des note: "))
# for i in range(1, N+1):
#     L1.append(float(input(f"Entrez la note numero {i}: ")))
# cp = 0
# for i in L1:
#     if i >= 10:
#         cp += 1
# print(f"Le nombre des note superieur a la moyen est: {cp}")


# Exercice 6:
# notes = []
# N = int(input("Entrez le nombre des notes: "))
# for i in range(1, N+1):
#     notes.append(float(input(f"Entrez la note numero {i}: ")))
# cpi = 0
# cpp = 0
# for i in range(len(notes)):
#     if notes[i] != 0:
#         if notes[i] % 2 == 0:
#             cpp += 1
#         else:
#             cpi += 1
# print(f"Le nombre des pairs est {cpp} et le nombre des impairs est {cpi}")


# # Exercice 7:
# T = []
# N = int(input("Entrez le nombre des notes: "))
# for i in range(1, N+1):
#     T.append(float(input(f"Entrez une valeur: ")))
# nb_occ = T.count(0)
# for i in range(nb_occ):
#     T.remove(0)
# print(T)


# # Exrecice 8:
# T = []
# N = int(input("Entrez le nombre des elements: "))
# for i in range(N):
#     T.append(int(input("Entrez une valeur: ")))
# T.sort(reverse=True)
# print(T)


# # Exercice 9:
# T = [print]
# N = int(input("Entrez le nombre des elements: "))
# for i in range(N):
#     T.append(int(input("Entrez une valeur: ")))
# TPOS = []
# TNEG = []
# for i in T:
#     if i < 0:
#         TNEG.append(i)
#     else:
#         TPOS.append(i)
# print("Pos", TPOS)
# print("NEG", TNEG)


# # Exercice 10:
# L = []
# for i in range(10):
#     x = int(input("Entrez une valeur: "))
#     while x < 0 or x > 20:
#         x = int(input("Entrez une valeur: "))
#     L.append(x)

# for i in range(21):
#     print(f"{i} a été répéter: {L.count(i)}")

# # Exercice 11:
# L1 = [5, 4, 5, 4, 5, 4]
# L2 = [5, 4, 5, 4, 5, 4]
# if L1 == L2:
#     print("Identique")
# else:
#     print("Pas identique")


# L = ["s","a","l","u","t"]
# def jeuMot(L):
#     k = 0
#     for i in range(len(L)):
#         print("*", end="")
#         for j in range(i, -1, -1):
#             print(L[j], end="*")
#         print()
# def jeuMotInverse():
#     for i in range(len(L)):
#         for j in range(i):
#             print(" ", end=" ")
#         print("*", end="")/
#         for j in range(i, len(L)):
#             print(L[j], "*")
#         print()
# print(jeuMotInverse())


# L = [4, 5, 4, 8, 7, 8, 8]

# max1 = max(L)
# for i in range(L.count(max1)):
#     L.remove(max1)
# print(L)


# min = L[0]
# for i in range(len(L)):
#     if L[i] <= min:
#         min = L[i]
#         posmin = i

# L[0], L[posmin] = L[posmin], L[0]
