import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import matplotlib.dates as dates
import datetime as dt
import locale

import pdb; pdb.set_trace()

df = pd.read_csv('dataset/ppz-jan-fev-2017.csv')

# show info about that dataset
print('Python pra Zumbis dataset head: ', df.head())

def to_date(value):
    return dt.datetime(2017, 1, 1) + dt.timedelta(hours=value)

# creating date column
df['date'] = df['hour'].apply(to_date)

del df['hour']

df.set_index(['date'], inplace=True)

# show info about that dataset with data
print('Python pra zumbis dataset head with data: ', df.head())

fig, ax = plt.subplots()

# convert pandas datetime object to python conventional datetime object
ax.plot_date(df.index.to_pydatetime(), df['views'], 'b-')

ax.xaxis.set_minor_locator(dates.DayLocator(bymonthday=range(5, 32, 5)))
ax.xaxis.set_minor_formatter(dates.DateFormatter('%d'))
ax.xaxis.set_major_locator(dates.MonthLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%b'))
ax.xaxis.grid(True, which='minor')
ax.yaxis.grid()
plt.tight_layout()
plt.savefig('test_17')
