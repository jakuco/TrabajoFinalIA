ruta_csv = '../data/EDV_2023_clasificacion.csv'
ruta_csv_limpio = '../data/EDV_2023_clasificacion_limpio.csv'

# Leer el archivo
with open(ruta_csv, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# limpiar las líneas
cleaned_lines = []
for line in lines:
    cleaned_line = ';'.join(item.strip() for item in line.split(';'))
    cleaned_lines.append(cleaned_line)

# guarda cada línea en el archivo
with open(ruta_csv_limpio, 'w', encoding='utf-8') as outfile:
    for line in cleaned_lines:
        outfile.write(line + '\n')
