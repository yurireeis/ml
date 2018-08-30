import matplotlib.pyplot as plt
import pandas as pd
import seaborn
import pydataset

df_air_passengers = pydataset.data('AirPassengers')

# AirPassengers dataset head
print('AirPassengers: ', df_air_passengers.head())

plt.figure(0)

'''
If you wanna use a dispersion chart, you must invoke the scatter method instead of plot
'''
plt.scatter(df_air_passengers['time'], df_air_passengers['AirPassengers'])
plt.savefig('test_12')

plt.figure(1)

df_iris = pydataset.data('iris')

# Iris dataset head
print('Iris dataset start: ', df_iris.head())

# Iris dataset tail
print('Iris dataset end: ', df_iris.tail())

plt.scatter(df_iris['Sepal.Length'], df_iris['Sepal.Width'], sizes=50 * df_iris['Sepal.Length'])
plt.savefig('test_13')

'''
create another column (serie) with pandas apply method
apply method must receive a anonymous function that gets the value of each
element and apply some transformation
'''

def specie_color(x):
    if x == 'setosa': return 0
    if x == 'versicolor': return 1
    return 2

# create special number series and apply a method to set color
df_iris['SpeciesNumber'] = df_iris['Species'].apply(specie_color)

# Iris dataset head with new column
print('Iris dataset start: ', df_iris.head())

# Iris dataset tail with new column
print('Iris dataset end: ', df_iris.tail())

# dispersion plot again with brand new column setting colors
plt.scatter(
    df_iris['Sepal.Length'],
    df_iris['Sepal.Width'],
    sizes=df_iris['Petal.Length'],
    c=df_iris['SpeciesNumber'],
    cmap='viridis',
    alpha=0.4
)

plt.savefig('test_14')
