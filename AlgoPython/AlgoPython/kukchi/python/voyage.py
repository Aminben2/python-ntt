h1, m1 = int(input("heur de depart: ")), int(input("minute de depart: "))
h2, m2 = int(input("heur d'arrivee: ")), int(input("minute d'arrivee: "))

if h1 >= 24 or m1 > 59 or h2 >= 24 or m2 > 59:
    print("invalide!")
else:
    if h2>h1:
        if m2>m1:
            hd = h2-h1
            md = m2-m1
            print(f"\n{hd}hs:{md}mins")
        else:
            hd = h2-h1-1
            md = m2+60-m1
            print(f"\n{hd}hs:{md}mins")
    else:
        if m2>m1:
            hd = h2-h1+24
            md = m2-m1
            print(f"\n{hd}hs:{md}mins")
        else:
            hd = h2-h1+24-1
            md = m2+60-m1
            print(f"\n{hd}hs:{md}mins")
