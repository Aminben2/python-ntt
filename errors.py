try:
    num = float(input("inter a real number :"))
    print("ha howa number dyalk : {}".format(num))
except ValueError:
    print("hadak maxi real number ya had rejel")
else :
    print("rak nadi amigo")

class NegativeAgeException(Exception):
    pass

n = -5
if n < 0 :
    raise NegativeAgeException("the age cannot be negative")

