import pandas as pd

data = pd.read_csv('../data/EDV_2023_clasificacion_2.csv', delimiter=',', low_memory=False)

print(data.head())
print(data.columns)

cor_mat= data[:].corr()
corr_y = abs(cor_mat['cau_div'])
highest_corr = corr_y[corr_y > 0.25]
highest_corr.sort_values(ascending=True)
print(len(highest_corr))


#"Zonas sin especificar" de cod_pais1 y cod_pais2
#label_encoder = LabelEncoder()
#f['Kingdom'] = label_encoder.fit_transform(df['Kingdom'])
