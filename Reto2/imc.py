def imc(estatura, peso):
    return peso / estatura ** 2

peso = float(input('escriba su peso en (kg): '))
estatura = float(input("escriba su estatura en (m): "))

indice = imc(estatura, peso)

print("su IMC es:  {}".format(indice))
