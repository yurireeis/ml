import pandas as pd
import numpy as np

data = {
    'name': ['João', 'Maria', 'José', np.nan, 'Pedro', 'Judas', 'Tiago'],
    'sex': ['M', 'F', 'M', np.nan, 'M', 'M', np.nan],
    'age': [14, 13, np.nan, np.nan, 15, 13, 14],
    'grade': [4, 10, 7, np.nan, 8, 9, 7]
}

df = pd.DataFrame(data)

# data loss dataframe
print('data loss dataframe: ', df)

# dropping all bad data elements
print('data frame curated: ', df.dropna())

# dropping only all missing data elements (in that example, index 3)
print('data frame curated (only drop all missing data elements): ', df.dropna(how='all'))

# create a column all filled by nan values
df['serie'] = np.nan
print('create a new column with nan as default value: ', df)

'''
drop column filled only with nan values using the dropna method (pass as axis parameter)
(axis=1) is column, as (axis=0) is line
'''
print('dropping the column filled only with nan values: ', df.dropna(how='all', axis=1))

# setting only when specific thresh is reached (loss data)
print('drop only when specific thresh is reached: ', df.dropna(thresh=3))

# fill specific serie (column) with a value
# df['serie'] = df['serie'].fillna(8) === fillna with inplace as parameter
df['serie'].fillna(8, inplace=True)
print('fill serie column with 8: ', df)

# include age average nos campos vazios
df['age'].fillna(df['age'].mean(), inplace=True)
print('Dataset with age data loss filled with age average: ', df)

# filtering by results setting only the element that has name as sex as not null
print('only results that has name and sex as no null: ', df[df['name'].notnull() & df['sex'].notnull()])
