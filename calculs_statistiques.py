import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from fpdf import FPDF

# Charger les données
df = pd.read_csv('path/to/your/dataset.csv')

# Analyse exploratoire des données (EDA)
print(df.describe())
print(df.corr())

# Moyenne, Médiane, Écart-type, Variance, Covariance
stats = df.agg(['mean', 'median', 'std', 'var', 'cov']).transpose()
print(stats)

# Visualisations interactives
fig = px.histogram(df, x="column_name", title="Histogramme Interactif")
fig.show()

# Graphique
df.mean().plot(kind='bar')
plt.xlabel('Colonnes')
plt.ylabel('Moyenne')
plt.title('Moyenne des colonnes')
plt.show()

# Création d'un PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Rapport de Statistiques", ln=True, align='C')

for i, row in stats.iterrows():
    pdf.cell(200, 10, txt=f"{i} - Moyenne: {row['mean']}, Médiane: {row['median']}, Écart-type: {row['std']}", ln=True)

pdf.output("rapport_statistiques.pdf")