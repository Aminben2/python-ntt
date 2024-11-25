d = {"TDI": ("TS", 1200), "TMSIR": ("T", 1300),
     "TRI": ("TS", 1100), "INFO": ("TS", 900)}

NomF = input("Entrez le nom de fliére: ")
value = d[NomF]
valeur = list(value)
del valeur[-1]
print(valeur)
