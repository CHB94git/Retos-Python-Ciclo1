def CalculadoraRectangulo(ancho:float, largo:float)->str:
    
    perimetro = (ancho*2) + (largo*2)
    area = ancho*largo
    print("El cuadrado tiene un perímetro de: "  +str(perimetro) +" y un área de: "  +str(area))

#Ingresar los parámetros con un solo decimal
CalculadoraRectangulo(3.0, 2.5)

