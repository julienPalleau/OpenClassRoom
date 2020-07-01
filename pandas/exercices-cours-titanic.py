# cours panda: https://openclassrooms.com/fr/courses/4452741-decouvrez-les-librairies-python-pour-la-data-science/5558996-passez-de-numpy-a-pandas
import numpy as np
import pandas as pd
import os
import seaborn as sns

famille_pandas = [
    [100, 5, 20, 80],
    [50, 2.5, 10, 40],
    [110, 6, 22, 80],
]
famille_pandas_numpy = np.array(famille_pandas)
famille_pandas_df = pd.DataFrame(famille_pandas_numpy, index=[
    'maman', 'bebe', 'papa'], columns=['pattes', 'poil', 'queue', 'ventre'])
print(famille_pandas_df)


# acceder à une colonne du tableau
print("\n", famille_pandas_df.ventre)

# acceder à une ligne: deux facons:
# premiere facon:
print("\n", famille_pandas_df.loc["papa"])
# deuxieme facon:
print("\n", famille_pandas_df.iloc[2])

# on peut faire du filtrage
print("\n", famille_pandas_df[famille_pandas_df.ventre == 80])

# on peut concatener deux data frame pour en faire un autre
autres_pandas = pd.DataFrame(
    [[105, 4, 19, 80], [100, 5, 20, 80]], columns=famille_pandas_df.columns)

tous_les_pandas = famille_pandas_df.append(autres_pandas)

print("\n", tous_les_pandas)

# on peut enlever les doublons
print("\n", tous_les_pandas.drop_duplicates())

# on peut lire un fichier csv
data = pd.read_csv(
    "C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\OpenClassroom\\pandas\\pandas.csv", sep=";")
print(data)

# on va prendre en exemple les donnees des survivants du titanic grace à la lib seaborn
titanic = sns.load_dataset('titanic')
print("\n", titanic.head())

# Enlever les doublons sur les ages
print("\n", titanic.age.unique())

print("\n", titanic.describe())

# Enlever toute les donnees manquantes
titanic = titanic.dropna()
print("\n", titanic.head())

# Nbre de survivants par classe et par sexe
# tableau croises dynamique
print("\n", titanic.pivot_table('survived',
                                index='sex', columns='class', aggfunc="sum"))

titanic.dropna(inplace=True)
age = pd.cut(titanic['age'], [0, 18, 80])
print("n", titanic.pivot_table('survived', ['sex', age], 'class'))

# Effectuez les operations d'algebre relationnelle sur les DataFrames
ser = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("\n")
print(ser)

data = [{'a': i, 'b': 2*i} for i in range(3)]
df = pd.DataFrame(data)
print("\n")
print(df)
