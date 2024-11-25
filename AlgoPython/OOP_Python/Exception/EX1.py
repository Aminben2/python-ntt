# # Exercice 1
# try:
#     age = int(input('Entrez votre age: '))
#     if age <= 0:
#         raise Exception()
#     print(f"Votre age est: {age}")
# except ValueError as e:
#     print('Entrez un nompbre')
# except:
#     print('Age doit étre superieur à 0')

# Exercice 2
# from math import sin


# def sinc(x):
# try:
#     res = sin(x)/x
#     return res
# except ZeroDivisionError:
#     return 1
#     if x is str:
#         raise Exception()
#     else:
#         if float(x) == 0:
#             return 1
#         else:
#             return sin(float(x))/float(x)

# try:
#     a = int(input('Entrez la valeur de x: '))
#     print(sinc(a))
# except Exception as e:
#     print(e)

# x = int(input('Entrez la valeur de x: '))
# print(sinc(x))

# # Exercise 3
try:
    nom = input('Entrez le nom du fichier')
    with open(nom+'.txt', 'r') as f:
        print(f.read())
except IOError as e:
    print(e)
except:
    print("Error")
