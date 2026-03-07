import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('iris_data.csv')

# question 1
print(data.columns)
print(data.dtypes)
print(data.shape)

# data.boxplot(by= 'species', figsize=(10, 8))

# queston 2
data['species'] = data.species.str.replace('iris', '')
# data['species'] = data.species.apply(lamda x: x.replace('iris', ''))

#question 3
# data.species.value_counts()
data_discription = data.describe()
# print(data_discription.head(10))

data.loc['range'] = data_discription.loc['max'] - data_discription.loc['min']
print(data_discription.head(10))

data_discription.rename({'25%':'median'}, inplace=True)
out_field = ['count', 'mean', 'min', 'median']
print(data_discription.loc[out_field])


#question 4
data.groupby('species').mean()
data.groupby('species').agg(['mean', 'max'])

#qestion 6
ax = plt.axes()
plt.scatter(data.petal_length, data.petal_width)
ax.set(xlabel = 'Lenght', ylabel='width', title='graph')

#qestion 7
ax = plt.axes()
plt.hist(data.petal_length, bins=25)
ax.set(xlabel = 'Lenght', ylabel='Frequency', title='graph')

data = pd.read_csv('iris_data.csv')
data.head()

#starting new project new example part 2
sns.set()
df = pd.read_csv('Ames_Housing_Data.tsv', sep='\t')
# df.head()
df.info()
df['Gr Liv Area'].hist()