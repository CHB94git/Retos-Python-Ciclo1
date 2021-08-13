import pandas as pd

def analisis_covid_ciclo_tipo(ruta_archivo: str)->dict:
    
    def ciclo_vital(edad)-> str:
        if edad <= 5:
            return "Primera infancia"
        elif edad <= 11:
            return "Infancia"
        elif edad <= 18:
            return "Adolescencia"
        elif edad <= 26:
            return "Juventud"
        elif edad <= 59:
            return "Adultez"
        else: 
            return "Persona Mayor"

    #Validate
    if ruta_archivo[-3:] != 'csv':
        return "Formato de archivo no válido"
   
    #Algorithm
    try:
        dataF = pd.read_csv(ruta_archivo)
        
        dataF_analisis = pd.DataFrame()
        dataF_analisis["Tipo"] = dataF["Tipo"].apply(str.upper)
        dataF_analisis["Ciclo"] = dataF["Edad"].apply(ciclo_vital)
        
        dataF_group = dataF_analisis.groupby(["Ciclo", "Tipo"]).size()

        return dataF_group.unstack().to_dict()
   
    except:
        return "Error procesando el archivo"

print(analisis_covid_ciclo_tipo("archivo.txt"))
print(analisis_covid_ciclo_tipo("archivo.xls"))
print(analisis_covid_ciclo_tipo("archivo.malo.txt"))
print(analisis_covid_ciclo_tipo("https://raw.githubusercontent.com/cesardiaz-utp/MisionTIC2022-Ciclo1-FundamentosDeProgramacion/main/clase16/Casos_positivos_de_COVID-19_en_ColombiaDiezMil.csv"))
