import time
mins = int(input("Entrer Les minutes: "))
sec = int(input("Entrer Les secondes: "))

num_of_secs = mins*60+sec
for i in range(0, num_of_secs):
    m, s = int(num_of_secs/60), int(num_of_secs % 60)
    print(f'{m}:{s}')
    time.sleep(.1)
    num_of_secs -= 1

print('Arrete')

'''
Algorithme CountDown
Variables mins, secs, m, s, num_of_secs: entier
Debut
	ecrire("entrer les minutes")
	lire(mins)
	ecrire("entrer les secondes")
	lire(secs)

	num_of_secs <- mins*60 + secs
	pour i allant de 0 à num_of_secs fair
		m <- num_of_secs / 60
		s <- num_of_secs % 60
		ecrire(m,':',s)
		num_of_secs <- num_of_secs - 1

	ecrire("Arrete!")

'''
