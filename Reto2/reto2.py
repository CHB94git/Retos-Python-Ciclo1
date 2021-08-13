def calcularSerie(nombre, peso, altura):

    imc = (peso / (altura**2))

    if imc < 18.5 or imc > 30:
        res = "{'nombre': "+"'"+str(nombre.upper())+"'"+", "+"'peso': "+str(peso)+", "+"'altura': "+str(altura)+", "+"'"+str("imc': '%.1f"%imc)+"'"+", "+"'programa': "+"'principiante', "+ "'valor': "+ "150000}"
        print(res)

    elif imc >= 25 and imc < 29.9:
        res = "{'nombre': "+"'"+str(nombre.upper())+"'"+", "+"'peso': "+str(peso)+", "+"'altura': "+str(altura)+", "+"'"+str("imc': '%.1f"%imc)+"'"+", "+"'programa': "+"'intermedio', "+ "'valor': "+ "170000}"
        print(res)

    elif imc >= 18.5 and imc < 24.9:
        res = "{'nombre': "+"'"+str(nombre.upper())+"'"+", "+"'peso': "+str(peso)+", "+"'altura': "+str(altura)+", "+"'"+str("imc': '%.1f"%imc)+"'"+", "+"'programa': "+"'plus', "+ "'valor': "+ "200000}"
        print(res)

calcularSerie("jhon", 82.4, 1.95)

    