def etudiants(chaine):
	etudiants_info = chaine.splitlines()
	etudiants = {}
	for i in etudiants_info:
		et = i.split(';')
		for e in range(len(et)):
			etudiants[et[0]] = f'{et[1]} {et[2]}'
	return etudiants



chaine_etudiants = """213615200;BESNIER;JEAN
213565488;DUPOND;MARC 
214665555;DURAND;JULIE"""

print(etudiants(chaine_etudiants))

# for k,v in etudiants(chaine_etudiants).items():
# 	print(k,':', v)