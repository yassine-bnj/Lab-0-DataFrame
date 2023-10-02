import pandas as pd
import matplotlib.pyplot as plt

# Question 1 : Création d'un DataFrame « df_p » 
data = {
    'Pays': ['États-Unis', 'Chine', 'Inde', 'Japon'],
    'Population': [331002651, 1439323776, 1380004385, 126476461],
    'Superficie (km²)': [9629091, 9640011, 3287263, 377972],
    'Taux de croissance annuel (%)': [0.6, 0.4, 1.1, -0.2]
}

df_p = pd.DataFrame(data)

print(df_p)

# Question 2: Transformation de dataframe en un dictionnaire nommé « dict_pays ».
dict_pays = df_p.to_dict(orient='records')

print(dict_pays)

# Question 3: Trie des éléments du dictionnaire par ordre croissant de la population
dict_pays_trie = sorted(dict_pays, key=lambda x: x['Population'])

print(dict_pays_trie)
# Question 4:  création d'un graphique à barres représentant la population de chaque
# pays du DataFrame. L'axe des x contient les noms des pays et l'axe des y  représente la population.
plt.bar(df_p['Pays'], df_p['Population'])
plt.xlabel('Pays')
plt.ylabel('Population')
plt.title('Population par pays')
plt.show()
#création d'un graphique en nuage de points (scatter plot)
# représentant la relation entre la superficie et le taux de croissance annuel des pays du DataFrame créé
# dans la question 1. L'axe des x  représente la superficie et l'axe des y  représente le taux de
# croissance annuel.

plt.scatter(df_p['Superficie (km²)'], df_p['Taux de croissance annuel (%)'], color='blue')
plt.xlabel('Superficie (km²)')
plt.ylabel('Taux de croissance annuel (%)')
plt.title('Relation entre la Superficie et le Taux de croissance annuel')
plt.grid(True)
plt.show()
