mdp = "Bonjour"
rep = "Minou"
Nb = 1
MDP = input("Entrez votre mot de passe: ")
while mdp != MDP and Nb != 3:
	MDP = input("Entrez votre mot de passe: ")
	Nb += 1

if mdp == MDP:
	print("Bonjour!")
else:
	REP = input("Votre Comte est blocké. C'est quoi le nom de votre chat? ")
	if REP == rep:
		print("Bonjour!")
	else:
		print("Votre compte est blocké")

'''Algorithme MDP 
Constante mdp: "Bonjour",
	  rep: "Minou",
Variable Nb: entier
Debut
	Nb <- 0
	Répeter
		Ecrire("Entrez votre mot de passe")
		Lire(MDP)
		Nb <- Nb + 1
	Jusqua mdp = MDP ou Nb = 3
	Si mdp = MDP Alors
		Ecrire("Bonjour!")
	Sinon
		Ecrire("Votre Comte est blocké. C'est quoi le nom de votre chat?")
		Lire(REP)
		Si REP = rep Alors
			Ecrire("Bonjour!")
		Sinon
			Ecrire("Votre compte est blocké")
		FinSi
	FinSi
Fin
'''
