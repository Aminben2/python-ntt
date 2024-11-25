# level 0
def fillingDictV0():
	d = dict()
	print("entrez '0' pour fermer le programme.")
	nomStg = input("Entrer le nom de stagiaire: ")

	while nomStg != '0':
		noteStg = float(input("Entrer sa note: "))
		# d[nomStg] = noteStg
		d.update({nomStg:noteStg})
		nomStg = input("Entrer le nom de stagiaire: ")
	return d

# level 1
def fillingDictV1():
	notes = {}
	nb = int(input("Entrez le nombre des stagiaire: "))
	n = int(input("Entrer le nombre des notes: "))

	for i in range(nb):
		lstNotes = []
		nomStg = input("Entrer le nom de stagiaire: ")
		for j in range(n):
			noteStg = float(input("Entrer sa note: "))
			lstNotes.append(noteStg)
		notes.update({nomStg:lstNotes})
	return notes


# level 2
def fillingDictV2():
	notes = {}
	nb = int(input("Entrez le nombre des stagiaire: "))
	n = int(input("Entrer le nombre des notes: "))

	for i in range(nb):
		dictNotes = {}
		nomStg = input("Entrer le nom de stagiaire: ")
		for j in range(n):
			noteStg = float(input("Entrer sa note: "))
			dictNotes[f'M10{j+1}'] = noteStg 
			
		notes.update({nomStg:dictNotes})
	return notes

print(fillingDictV2())

# s = 'y u s u f'
# print(s.split())

