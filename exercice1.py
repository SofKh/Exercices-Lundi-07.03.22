import math

def carre_racine(base):
    if base>0 :
        return base*base, math.sqrt(base)
    else :
        return base*base, 0


n=int(input("Rentrer un numero: "))

carre, racine = carre_racine(n)


if racine==0 :
    print(f"le carré de {n} est {carre}")
else:
    print(f"le carré de {n} est {carre} ET sa racine carré {racine}")

#fin