char = ord(input("Entrez une lettre: "))

# methode 1
if ord('a') <= char <= ord('z'):
	print("La lettre saisie est Minuscule")
elif ord('A') <= char <= ord('Z'):
	print("La lettre saisie est Majuscule")
elif ord('0') <= char <= ord('9'):
	print('number')
else:
	print("C'est une symbol")


# methode 2
# if 'a' <= char <= 'z':
# 	print("La lettre saisie est Minuscule")
# elif 'A' <= char <= 'Z':
# 	print("La lettre saisie est Majuscule")
# elif '0' <= char <= '9':
# 	print('number')
# else:
# 	print("C'est une symbol")
