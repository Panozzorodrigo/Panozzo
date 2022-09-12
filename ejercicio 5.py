def recortar(numero, limit_inf, limit_sup):
    if numero > limit_inf:
        print(limit_inf, "es inferior al número a recortar")
    elif numero < limit_sup:
        print(limit_sup, "es superior al número a recortar")
    else:
        print(numero)

recortar(15, 5, 10)
