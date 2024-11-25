

usern = int(input("entrer un nombre "))
grandn = usern
position = 1
for i in range(1, 4):
    usern = int(input("entrer un nombre "))
    if usern > grandn:
        grandn = usern
        position = i+1

print("le max est ", grandn, "position", position)

