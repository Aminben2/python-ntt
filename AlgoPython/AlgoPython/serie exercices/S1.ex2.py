'''
Algorithme MDP
Constante mdp: "Bonjour",
			rep: "Minou",
Variable Nb: entier
Debut
	Nb <-- 0
	Répeter
		Ecrire("Entrez votre mot de passe")
		Lire(MDP)
		Nb <-- Nb + 1
	Jusqua mdp = MDP ou Nb = 3
	Si mdp = MDP Alors
		Ecrire("Bonjour!")
	Sinon
		Ecrire("Votre Comte est blocké reponder a se question. C'est quoi la reponse secrete")
		Lire(REP)
		Si REP = rep Alors
			Ecrire("Bonjour!")
		Sinon
			Ecrire("Votre comte est blocké")
		FinSi
	FinSi
Fin
'''

n = 0
mdp = input("Entrez votre mot de passe: ")
while mdp != "Bonjour" and n != 2:
    n += 1
    mdp = input("Entrez votre mot de passe: ")
if mdp == "Bonjour":
    print("Autentification reussie")
else:
    rep = input("Entrez la reponse a la questioin secret")
    if rep == "Minou":
        print("Authentification reussie")
    else:
        print("Compte bloqué")
