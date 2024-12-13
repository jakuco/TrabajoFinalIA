import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/EDV_regresion.csv", sep=";")

plt.figure(figsize=(10, 5))
#fecha_formateada;tasa_diaria
plt.plot(df['fecha_formateada'], df['tasa_diaria'])

# Personalizar el gráfico
plt.title('Ejemplo de gráfico con fechas')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.grid(True)

# Mostrar el gráfico
plt.show()
