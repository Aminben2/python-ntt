def f4(pre, age):
    if age < 20:
        print("Vous étes un enfant")
    elif age < 50:
        print("Vous étes adulte")
    elif age >= 50:
        print("Vous étes agé")
    pre = input("Entrez votre prenom: ")
    age = input("Entrez votre age: ")


print(f4)
