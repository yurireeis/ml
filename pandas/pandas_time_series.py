import pandas as pd
from db import DB

database = DB(filename='logs.sqlite3', dbtype='sqlite')
database.tables

# log dataframe
df = database.tables.log.all()

# sqlite work with date as string
print('column types: ', df.dtypes)

# using pandas function to parse to datetime format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S.%f')
print('look for the parsed date in the column: ', df.dtypes)

'''
set index to better performance and filtering by the topic (in this case
is the date)
'''
df.set_index(['date'], inplace=True)

# search date by 2017 year
print('2017 values: ', df['2017'])

# search date of 2017, month 1, day 3 and start at 10 AM
print('2017-01-03 10 AM values: ', df['2017-01-03 10'])
