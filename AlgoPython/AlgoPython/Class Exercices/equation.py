a = float(input("Entrer le premier coefficient : "))
b = float(input("Entrer le deuxieme coefficient : "))
c = float(input("Entrer le troisieme coefficient : "))
import math
if a == 0:
    if b == 0:
        print("L'equation admit pas de solution")
    else:
        print(f"La solution est:  {-c / b}")
else :
    D = math.pow(b,2)-(4 * a * c)
    if D < 0 :
        print( "Equation invalide" )
    elif D == 0:
        print (f"La solution est : {-b/(2*a)}")
    else: 
        print( f"Les deux solutions sont: x1 = {(-b - math.sqrt(D))/(2*a)} et x2 = {(-b + math.sqrt(D))/(2*a)}")