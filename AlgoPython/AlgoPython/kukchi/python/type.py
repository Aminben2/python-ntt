def typo(x):
    xt = str(type(x))
    sq1 = xt.find("'")
    sq2 = xt.find("'>", sq1)
    return xt[sq1+1:sq2]

x = type("s") == typo(3)
print(x, typo(3))
