def CalculadoraRectangulo():
   
    #Datos solicitados por teclado al usuario

    ancho = float(input("Ingresa el ancho del rectángulo, con 1 solo decimal: "))
    largo = float(input("Ingresa el largo del rectángulo, con 1 solo decimal: "))
    perimetro = (ancho*2) + (largo*2)
    area = ancho*largo
    print(f"El cuadrado tiene un perimetro de: {perimetro} y un área de: {area}")
    pass

CalculadoraRectangulo()



