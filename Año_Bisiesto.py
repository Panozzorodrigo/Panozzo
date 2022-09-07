def bis_o_no_bis(numero):
    if numero % 4 == 0 and numero % 100 != 0:
        print(numero, "es un año Bisiesto")
    elif numero % 4 == 0 and numero % 100 == 0 and numero % 400 == 0:
        print(numero, "es un año Bisiesto")
    else:
        print(numero, "no es un año Bisiesto")


año = bis_o_no_bis(int(input("Ingrese un año: ")))
