def simulador_prestamo_yo_le_presto(prestamo={})-> dict:
    
    EA = prestamo["interes anual"]
    Meses = (prestamo["cuotas"])
    SaldoAFinanciar = prestamo["gastos documentacion"] + prestamo["valor"]
    
    TMV = (((1+EA/100)**(1/12)-1))
    Cuota = float("{0:.2f}".format(round((SaldoAFinanciar)/((1-(1+TMV)**-Meses)/TMV))))
    Amortizacion = []
    CuotaF = Cuota
    
    for i in range (Meses):
        Intereses = float("{0:.2f}".format(SaldoAFinanciar * TMV))
        CapitalAbo = float("{0:.2f}".format(Cuota - Intereses))
        NuevoSaldo = float("{0:.2f}".format(SaldoAFinanciar - CapitalAbo))

        if Meses == (i+1):
            CapitalAbo = float("{0:.2f}".format(NuevoSaldo + CapitalAbo))
            Cuota = float("{0:.2f}".format(NuevoSaldo + Cuota))
            NuevoSaldo = float("{0:.2f}".format(0))
        Lista = (i+1, CapitalAbo, Intereses, Cuota, NuevoSaldo)
        i+=1
        SaldoAFinanciar = float("{0:.2f}".format(SaldoAFinanciar - CapitalAbo))
        Amortizacion.append(Lista)

    prestamo = {'saldo financiar': prestamo["valor"]+prestamo["gastos documentacion"], 'cuota': CuotaF, 'amortizacion': Amortizacion}
    return prestamo

print(simulador_prestamo_yo_le_presto({'valor': 2000000.00, 'gastos documentacion': 0.0, 'cuotas': 6, 'interes anual': 28.99}))
print(simulador_prestamo_yo_le_presto({'valor': 1200000.00, 'gastos documentacion': 100000.0, 'cuotas': 12, 'interes anual': 25.13}))
