def recortar(numero, limit_inf, limit_sup):
    if numero < limit_inf:
        return(limit_inf, "es inferior al número a recortar")
    elif numero > limit_sup:
        return(limit_sup, "es superior al número a recortar")
    else:
        return(numero)

print(recortar(15, 5, 10))
