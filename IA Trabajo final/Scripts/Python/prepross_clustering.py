
import pandas as pd

import pandas as pd
import re

""" Utilizado para verificar cuales son las variables con mas corrrelación """

data = pd.read_csv('EDV_2023_tasas.csv', delimiter=';', low_memory=False)

columnas = [
    "cant_insc",
    "parr_insc",
    "mes_insc",
    "dia_insc",
    "fecha_insc",
    "cant_hab2",
    "parr_hab2",
    "cant_hab1",
    "parr_hab1",
    "mes_div", 
    "dia_div",
    "fecha_div",
    "mes_mat",
    "dia_mat",
    "fecha_mat",
    "mes_nac1",
    "dia_nac1",
    "fecha_nac1",
    "mes_nac2",
    "dia_nac2",
    "fecha_nac2",
    "anio_nac2",
    "anio_nac1",
    "anio_div",
    "anio_mat", 
    "prov_insc",
    "anio_insc",
    "nac_1",
    "nac_2",
    #"nac"
    "sexo_1",
    "sexo_2"
]

data = data[['edad_1', 'edad_2', 'hijos_1', 'hijos_2', 'dur_mat','cau_div', 'prov_insc']]
#data = data.drop(columns=columnas, axis=1)
data.reset_index(drop=True, inplace=True)

print(data.dtypes)
print(data.shape[0])
for column in data.columns:
    indexNames = data[data[column] == 'Sin información'].index
    data.drop(indexNames, inplace=True)
print(data.shape[0])
print(data['cau_div'].value_counts())

data.to_csv("../data/EDV_2023_clustering.csv", sep=";", index=False)
