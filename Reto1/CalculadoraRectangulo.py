def calculadoraRectangulo(ancho:float, largo:float)-> str:
    
    perimetro = (ancho*2) + (largo*2)
    area = ancho*largo
    
    result = (f"El cuadrado tiene un perímetro de: " +str("%.1f"%perimetro) +" y un área de: " +str("%.1f"%area))
    print(result)

calculadoraRectangulo(6.4, 2.5)
