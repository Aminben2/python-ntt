# Nb = int(input(f"Entrez une nombre: "))

# while Nb <= 0:
#     Nb = int(input(f"Entrez une nombre: "))
# if Nb == 0 or Nb == 1 :
#     print(f"{Nb} N'est pas Premier")
# elif Nb == 2:
#     print(f'{Nb} est Premier')
# else:
#     test = False
#     for i in range(2, int(Nb/2)):
#         if (Nb % i == 0):
#             test = True
#             break

#     if test == False:
#         print(f"{Nb} Est Un Nombre Premier")
#     else:
#         print(f"{Nb} n'est pas Un Nombre Premier")


i = 2
nb_premiers = 0
lst = list()
while nb_premiers < 100:
    if i == 2:
        print(f'{i}')
        # lst.append(i)
        i += 1
        nb_premiers += 1
    else:
        test = False
        for j in range(2, int(i/2)):
            if (i % j == 0):
                test = True
                break

        if test == False:
            print(f"{i}")
            # lst.append(i)
            i += 1
            nb_premiers += 1
        else:
            i += 1
# print(len(lst))

print(17%5)