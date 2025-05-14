import pandas as pd
import matplotlib.pyplot as plt

# Datos inventados de enfermedades
data = {
    'Enfermedad': ['Gripe', 'COVID-19', 'Ébola', 'Sarampión', 'Varicela'],
    'Casos': [10000, 5000, 300, 2000, 1500],
    'Muertes': [10, 300, 200, 5, 1]
}
#Comentario por javier
df = pd.DataFrame(data)
df['Tasa Mortalidad (%)'] = (df['Muertes'] / df['Casos']) * 100

# Enfermedad más peligrosa (mayor tasa de mortalidad)
mas_peligrosa = df.loc[df['Tasa Mortalidad (%)'].idxmax()]
# Enfermedad menos peligrosa (menor tasa de mortalidad)
menos_peligrosa = df.loc[df['Tasa Mortalidad (%)'].idxmin()]

# Gráfico de barras de tasa de mortalidad
plt.figure(figsize=(8, 5))
plt.bar(df['Enfermedad'], df['Tasa Mortalidad (%)'], color='skyblue')
plt.title('Tasa de Mortalidad por Enfermedad')
plt.xlabel('Enfermedad')
plt.ylabel('Tasa de Mortalidad (%)')

# Resaltar la más y menos peligrosa
plt.bar(mas_peligrosa['Enfermedad'], mas_peligrosa['Tasa Mortalidad (%)'], color='red', label='Más peligrosa')
plt.bar(menos_peligrosa['Enfermedad'], menos_peligrosa['Tasa Mortalidad (%)'], color='green', label='Menos peligrosa')
plt.legend()

plt.tight_layout()
plt.show()

print("NO FUNCIONA EL PIP:'v")