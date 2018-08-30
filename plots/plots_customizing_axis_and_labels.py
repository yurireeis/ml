import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/reported.csv')

# verify info about dataset
print('infos: ', df.head())

# fill nan's with zero
df.fillna(0, inplace=True)

'''
to have more control over the figure/axis, you must create subplots object
'''
fig, ax = plt.subplots()

'''
plt.plot is a shortcut to ax object, because of this the instance has the same
way to instantiate to plt.plot
'''
ax.plot(df['Year'], df['crimes.total'], '-r')
ax.plot(df['Year'], df['crimes.person'], '-b')

# positioning legend
ax.legend(loc='upper left')

# setting x label and y label
ax.set_xlabel('Year')
ax.set_ylabel('Quantity')

# set title
ax.set_title('Crimes: Total x Person')

# changing x axis limit
ax.set_xlim([df['Year'].min(), df['Year'].max()])

plt.savefig('test_16')
