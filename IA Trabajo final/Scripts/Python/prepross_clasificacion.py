import pandas as pd
import re

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

#coincidencias = data[data['anio_mat'] == data['anio_div']]

#cantidad_divorcios_mat_2022_2023 = data[(data['anio_mat'] == 2022) | (data['anio_mat'] == 2023)]

#print(cantidad_divorcios_mat_2022_2023.shape[0])

data = data.drop(columns=columnas, axis=1)
data.reset_index(drop=True, inplace=True)

print(data.dtypes)
#data.columns = data.columns.str.strip()
#data.dropna(how='all', inplace=True)

# Función para eliminar espacios en blanco después de las comas
"""def remove_spaces_after_commas(value):
    if isinstance(value, str):
        return re.sub(r',\s+', ';', value)
    return value
"""

# Aplicar la función a todas las celdas del DataFrame
#data = data.applymap(remove_spaces_after_commas)
#data['hijos1'] = data['hijos_1']
print(data.shape[0])
for column in data.columns:
    indexNames = data[data[column] == 'Sin información'].index
    data.drop(indexNames, inplace=True)
print(data.shape[0])
print(data['cau_div'].value_counts())

data.to_csv("EDV_2023_clasificacion.csv", sep=";", index=False)