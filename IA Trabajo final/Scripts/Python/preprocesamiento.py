import pandas as pd

"""     Se usa los índices de violencia de genero según la provincia con el fin 
	de obtener nuevas variables para hacer el análisis de datos
	te toma encuenta la provincia en donde se casaron
	En los datos solo se toman las parejas que se divorcian en el mismo lugar que viven"""

# Definir el diccionario de tasas de violencia intrafamiliar por provincia
tasas_violencia = {
    "Azuay": 0.527,
    "Bolívar": 0.331,
    "Cañar": 0.551,
    "Carchi": 0.446,
    "Chimborazo": 0.393,
    "Cotopaxi": 0.431,
    "El Oro": 0.462,
    "Esmeraldas": 0.486,
    "Galápagos": 0.338,
    "Guayas": 0.405,
    "Imbabura": 0.471,
    "Loja": 0.436,
    "Los Ríos": 0.342,
    "Manabí": 0.335,
    "Morona Santiago": 0.606,
    "Napo": 0.588,
    "Orellana": 0.428,
    "Pastaza": 0.519,
    "Pichincha": 0.445,
    "Santa Elena": 0.369,
    "Santo Domingo de los Tsáchilas": 0.418,
    "Sucumbíos": 0.468,
    "Tungurahua": 0.489,
    "Zamora Chinchipe": 0.515
}

# según 2023
desempleo = {
    "Azuay": 3,
    "Bolívar": 0.7,
    "Cañar": 2.8,
    "Carchi": 4.5,
    "Cotopaxi": 1.8,
    "Chimborazo": 1.4,
    "El Oro": 5.6,
    "Esmeraldas": 9,
    "Galápagos": 4.2,
    "Guayas": 3.1,
    "Imbabura": 5.6,
    "Loja": 3.6,
    "Los Ríos": 2,
    "Manabí": 1.9,
    "Morona Santiago": 0.6,
    "Napo": 0.8,
    "Orellana": 1.3,
    "Pastaza": 1,
    "Pichincha": 7.5,
    "Santa Elena": 2.9,
    "Santo Domingo de los Tsáchilas": 1.9,
    "Sucumbíos": 2.7,
    "Tungurahua": 2,
    "Zamora Chinchipe": 2.5,
}


data = pd.read_csv('../data/EDV_2023.csv', delimiter=';', low_memory=False)

# Se crea una nueva columna basada en el diccionario de tasas de violencia
data['ts_violencia_prov_insc'] = data['prov_insc'].map(tasas_violencia)
data['ts_desempleo_prov_insc'] = data['prov_insc'].map(desempleo)

df = data[(data['prov_hab1'] == data['prov_hab2']) &  (data['sexo_1'] != data['sexo_2'])]

# Se refica que no haya errores en el filtrado de los datos.
print(data.shape[0])
print(df.shape[0])
print(data.head())

## Se empieza con el cambio de la causa de divorcio
print(df['cau_div'].value_counts())

# Se unen las categorias disponibles de los divorcios
# Obteniendo al final dos categorías; Mutuo consentimiento, Causal
categorias_divorcio_causal = [
    "El abandono injustificado de cualquiera de los cónyuges por más de seis meses ininterrumpidos",                          
    "El estado habitual de falta de armonía de las dos voluntades en la vida matrimonial",                                                                                                                                     
    "Los tratos crueles o violencia contra la mujer o miembros del núcleo familiar",                                           
    "El que uno de los cónyuges sea ebrio consuetudinario o toxicómano",                                                       
    "La condena ejecutoriada a pena privativa de la libertad mayor a diez años",                                                
    "El adulterio de uno de los cónyuges",                                                                                      
    "Las amenazas graves de un cónyuge contra la vida del otro",                                                                
    "Los actos ejecutados por uno de los cónyuges con el fin de involucrar al otro o a los hijos en actividades ilícitas",      
    "La tentativa de uno de los cónyuges contra la vida del otro"    
]

categorias_divorcio_consensual = [
    "Por mutuo consentimiento vía judicial",                                                                               
    "Por mutuo consentimiento vía notarial"  
]

nuevo_categoria_consensual = 'Mutuo consentimiento'
nuevo_categoria_causal = 'Causal'

# Se remplazan las categorías seleccionadas con el nuevo nombre
df['cau_div'] = df['cau_div'].replace(categorias_divorcio_causal, nuevo_categoria_causal)
df['cau_div'] = df['cau_div'].replace(categorias_divorcio_consensual, nuevo_categoria_consensual)

# Se eliminan las filas en el caso que no tengan una causa de divorcio
df = df[df['cau_div'] != 'Sin información']

df.reset_index(drop=True, inplace=True)

df.to_csv("../data/EDV_2023_tasas.csv", sep=";", index=False)
