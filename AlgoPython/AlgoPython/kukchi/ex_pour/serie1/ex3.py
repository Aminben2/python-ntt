import time
mins = int(input("Entrer Les minutes: "))
sec = int(input("Entrer Les secondes: "))

seconds_total = mins*60+sec
for i in range(0, seconds_total):
    m, s = int(seconds_total/60),int(seconds_total%60)
    print(f'{m}:{s}')
    time.sleep(1)
    seconds_total -= 1
    
print('Arret')

'''
Algorithme CountDown
Variables mins, secs, m, s, seconds_total: entier
Debut
	ecrire("entrer les minutes")
	lire(mins)
	ecrire("entrer les secondes")
	lire(secs)

	seconds_total <- mins*60 + secs
	pour i allant de 0 à seconds_total fair
		m <- seconds_total / 60
		s <- seconds_total % 60
		ecrire(m,':',s)
		seconds_total <- seconds_total - 1

	ecrire("Arrete!")
Fin
'''
