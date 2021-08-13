def simulador_prestamo_yo_le_presto(prestamo={})->dict:

    Valor = prestamo["valor"]
    EA = prestamo["interes anual"]
    Meses = (prestamo["cuotas"])
    SaldoFin = prestamo["gastos documentacion"] + Valor
    TMV = ((1+EA/100)**(1/12)-1)
    Cuota = round((SaldoFin/((1-(1+TMV)**-Meses)/TMV)),0)
    Amortizacion = []
    SaldoPend = Cuota

    for inc in range (Meses):
        Interes = round((SaldoFin*TMV),2)
        CapitalAbo = round((Cuota - Interes),2)
        Pend = round((SaldoFin - CapitalAbo),2)
        if inc==(Meses-1):
            CapitalAbo = round((Pend + CapitalAbo),2)
            Cuota = round((Pend + Cuota),2)
            Pend = float("{0:.2f}".format(0))
        Lista = (inc+1, CapitalAbo, Interes, Cuota, Pend)
        inc+=1
        SaldoFin = round((SaldoFin - CapitalAbo),2)
        Amortizacion.append(Lista)
    prestamo = {'saldo financiar': prestamo["valor"]+prestamo["gastos documentacion"], 'cuota': SaldoPend, 'amortizacion': Amortizacion}
    return prestamo

print(simulador_prestamo_yo_le_presto({'valor': 2000000.00, 'gastos documentacion': 0.0, 'cuotas': 6, 'interes anual': 28.99}))
print(simulador_prestamo_yo_le_presto({'valor': 1200000.00, 'gastos documentacion': 100000.0, 'cuotas': 12, 'interes anual': 25.13}))


