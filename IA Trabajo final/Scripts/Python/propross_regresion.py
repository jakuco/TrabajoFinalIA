
import pandas as pd
from datetime import datetime

# Crear un DataFrame de ejemplo con los meses
meses = {
    'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
    'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
}

anio_inicio = 2014
anio_fin = 2023

# Lista de todos los .csv
archivos = ['../data/data/EDV_'+str(fecha)+'.csv' for fecha in range(anio_inicio, anio_fin+1)]

divorsios_anual = {
    2014: 15.4,
    2015: 15.7,
    2016: 15.2,
    2017: 14.7,
    2018: 14.9,
    2019: 15.1,
    2020: 15.0,
    2021: 15.7,
    2022: 16,
    2023: 16.4
    }

total_anual = dict()

# Leer y combinar los datos de todos los archivos CSV en un solo DataFrame
dfs = []
for archivo in archivos:
    df = pd.read_csv(archivo, low_memory=False, sep=";", encoding="latin")
    
    # Formateo a una fecha que puede ser usar por los modelos de entrenamiento
    if not str(df['mes_div'][0]).isdigit():
        df = df[df['mes_div'].str.strip().isin(meses.keys())]
        df['fecha_formateada'] = df.apply(lambda row: datetime(int(row['anio_insc']), meses[row['mes_insc'].strip()], int(row['dia_insc'])), axis=1)
    else:
        df['fecha_formateada'] = df.apply(lambda row: datetime(int(row['anio_insc']), row['mes_insc'], int(row['dia_insc'])), axis=1)
    
    # Agregar el DataFrame al listado
    total_anual[df['anio_insc'].iloc[0]] = df.shape[0]
    dfs.append(df)

# Concatenar todos los DataFrames en uno solo
df_combinado = pd.concat(dfs, ignore_index=True)

# Generar un rango de fechas para el año completo
fecha_inicio = datetime(anio_inicio, 1, 1)
fecha_fin = datetime(anio_fin, 12, 31)
rango_fechas = pd.date_range(start=fecha_inicio, end=fecha_fin)

# Crear un DataFrame con el rango de fechas y establecer el conteo inicial en 0
conteo_fechas = pd.DataFrame(rango_fechas, columns=['fecha_formateada'])
conteo_fechas['repeticiones'] = 0

# Conteo de la cantidad de veces que se repite cada fecha en el DataFrame combinado
conteo_real = df_combinado['fecha_formateada'].value_counts().reset_index()
conteo_real.columns = ['fecha_formateada', 'repeticiones']

# Combinación de los conteos reales con el DataFrame de fechas completas
conteo_final = pd.merge(conteo_fechas, conteo_real, on='fecha_formateada', how='left')
conteo_final['repeticiones'] = conteo_final['repeticiones_y'].fillna(0).astype(int)

conteo_final = conteo_final.drop(columns=["repeticiones_x", "repeticiones_y"])
conteo_final['tasa_diaria'] = 0
aux = conteo_final.copy()

# se crea un  tasa diaria de divorcios según la tasa anual.
for i in range(len(conteo_final)):
    for anio in total_anual.keys():
        if str(anio) in str(aux.at[i, 'fecha_formateada']):
            conteo_final.at[i, 'tasa_diaria'] = aux.at[i, 'repeticiones']*divorsios_anual[anio]/total_anual[anio]

conteo_final = conteo_final.drop(columns=["repeticiones"])

tasa_minima = conteo_final['tasa_diaria'].min()
tasa_maxima = conteo_final['tasa_diaria'].max()

# Información de los datos
print(conteo_final['tasa_diaria'].mode())
print(conteo_final['tasa_diaria'].median())
print(conteo_final['tasa_diaria'].mean())
print("Tasa maxima", tasa_maxima)
print("Tasa minima", tasa_minima)

# Creación del dataset para la regresión
conteo_final.to_csv('../data/EDV_regresion.csv', index=False, sep=";")

proporcion = 0.80
indice = int(conteo_final.shape[0]*proporcion)


# Creación de los datos de prueba y entrenamiento
entrenamiento = conteo_final.iloc[:indice]
test = conteo_final.iloc[indice:]

entrenamiento.to_csv('../data/EDV_regresion_entre.csv', index=False, sep=";")
test.to_csv('../data/EDV_regresion_test.csv', index=False, sep=";")

# Ver el total de datos para el análisis
print("Total data:", conteo_final.shape[0])
print("Total Entrenamiento:", entrenamiento.shape[0])
print("Total Testeo:", test.shape[0])

