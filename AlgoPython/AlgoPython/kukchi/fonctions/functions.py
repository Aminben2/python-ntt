"""
Algoruthme Prog_princ
Variables L, l : reel

FONCTION calculSurfaceR(L: reel, l: reel):reel
	variables s:reel
	Debut
	s <- L*l
	returne s
FinFonction

Debut
ecrire("Entrer la Longueur et la Largeur")
lire(L, l)

calculSurfaceR(L, l)
Fin

"""
# ############################

# #kaggle.com
# def factorial(num):
# 	if num < 0:
# 		return 'invalid'
# 	elif num == 0:
# 		return '1'
# 	else:
# 		f = 1
# 		for i in range(1,num+1):
# 			f *= i
# 		return f


# print(factorial(int(input('number: '))))


# ############################

# def f2(a):
# 	for i in range(a):
# 		print("Hello")

# f2(3)

# def f3(a):
# 	for i in range(a):
# 		print('Hello')
# 	return 0 


# def hello(name, age):
# 	print(f'Bonjour {name}')
# 	if age < 20:
# 		print('tu est un enfants')
# 	elif age > 50



# ############################

'''
Algortithme prc
variables p, n
procédure pn(p,n:entier)
	Debut
	p <- p^n
	ecrire(p)
FinProcedure

Debut
ecrire("entrer p")
lire(p)
ecrire("entrer n")
lire(n)
pn()
'''
# ############################

# def pn(p, n):
# 	p **=n
# 	print(p)

# def pgcd(a,b):
#     if a < b:
#     	a = b
#     	b = a
 
#     max = 0
#     for i in range(1, b+1):
#     	if a % i == 0 and b % i == 0:
#     		if i > max:
#     			max = i
#     print(max)

# pgcd(56,42)


# ############################

def calc(a=1,b=2,c=6,d=8):
	print('{} + {} + {} + {} = {}'.format(a,b,c,d, a+b+c+d))

calc()

# ############################
'''

variables a,b: reel

Procédure perm(a,b: reel par adresse)
	variables c: reel
	c <- a
	a <- b
	b <- c
FinProcédure

Algorithme perm
variables a,b: reel
Debut
	ecrire("Entrer la valeur de a")
	lire(a)
	ecrire("Entrer la valeur de b")
	lire(b)
	
	perm(a,b)
Fin

'''










