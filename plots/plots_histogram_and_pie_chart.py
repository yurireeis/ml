import pandas as pd
import pydataset
import matplotlib.pyplot as plt
import seaborn as sns

df = pydataset.data('titanic')

# starter figure
plt.figure(0)

# count Frequency of results in each titanic class
print('Frequency of each class on titanic: ', df['class'].value_counts())

# plot in easy way for notebook
df['class'].value_counts().plot(kind='bar')

# plot for archive
plt.savefig('test_6')

# show the survivors rate
df['survived'].value_counts().plot(kind='bar')
plt.savefig('test_7')

# visualizing the class and group by survivors
survivors_by_class = df.groupby('survived')['class'].value_counts()
print('Who survived? ', survivors_by_class)

# class and quantity of survivors
class_and_survivors = df.groupby('class')['survived'].value_counts()
print('Survivors by class: ', class_and_survivors)

# creating a branding new figure
plt.figure(1)

# reading estados.csv info
estados = pd.read_csv('dataset/populacao_brasil.csv')

# show estados data
print('Estados dataframe head: ', estados.head())

# show histogram of estados
estados['total'].hist()
plt.savefig('test_9')

# recovering info about this plot (the second parameter is axis)
fig, ax = plt.subplots()

'''
first parameter: the dataframe
bins: numbers of intervals
'''
plt.hist(estados['total'], bins=15, orientation='horizontal')

# ax ticklabel is How the value in printed in the axis
ax.ticklabel_format(style='plain')
plt.savefig('test_10')

# percentage of each state vs. brazil population
estados['percent'] = estados['total'] / estados['total'].sum()

# state dataframe representation with population percentage against brazil population
print('State vs. Brazil population new column: ', estados.head())

# ploting pie chart with that info
'''
autopct: the value that comes in chart
'''
plt.pie(estados['percent'], labels=estados['estado'], autopct='%1.2f%%')
plt.savefig('test_11')
