s_base = float(input("Entrez votre salaire de base: "))
if s_base > 0 :
	if s_base < 4000:
		reponse = (input("est ce que to a une retraite comp?: "))
		if reponse != 'o' and reponse != 'O' and reponse != 'N' and reponse != 'n':
			print("reponse invalide")
		elif reponse == 'o' or reponse == 'O':
			r_comp = int(input("Combien? "))
			if r_comp != 200 and r_comp != 400 and r_comp != 600 :
				print("invalide")
			elif r_comp == 200:
				s_retrait = s_base
			elif r_comp == 400:
				s_retrait = s_base + 200
			elif r_comp == 600:
				s_retrait = s_base + 500
		else:
			s_retrait = s_base - 300
	elif s_base < 10000 and s_base > 4000:
		echelle = int(input("quelle echelle? "))
		if echelle > 11:
			s_retrait = s_base
		else:
			s_retrait = s_base - 200
	else:
		s_retrait = s_base
	print(f"votre salaire de retraite est {s_retrait}DH")
else:
	print("nombre invalide!")
