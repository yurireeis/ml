import pandas as pd
import numpy as np

df = pd.read_csv('dataset/primary_results.csv')

# looking for the headers of this dataframe
print('headers: ', df.head())

# length of dataframe
print('the length is: ', len(df))

# grouping by candidate (transform object in dataframe groupby object)
print('creating an groupby object (by candidate): ', df.groupby('candidate'))

'''
when you have a groupby object, you can associate an aggregate
aggreate is used to aggregate info by a column
(python has already implemented min and max functions)
aggregate is applied in numeric values
'''
print('aggregate by votes (min, average, max): ', df.groupby('candidate').aggregate({ 'votes': [min, np.mean, max] }))

# filter by number of votes to grab more information about
print('Hillary Clinton received more votes on: ', df[df['votes'] == 590502])

# aggregating by fraction_votes
print('aggregate by fraction_votes (min, average, max): ', df.groupby('candidate') \
    .aggregate({ 'fraction_votes': [min, np.mean, max] }))

# know about where candidates received one hundred percent votes
print('Show where candidates received 100% votes: ', df[df['fraction_votes'] == 1])

# look foward to locals where an specific candidate gained 100% percent of votes
print('Show here an specific candidate gained 100% votes: ', df[(df['fraction_votes'] == 1) & (df['candidate'] == 'Hillary Clinton')])

'''
create an anonymous function to filter values by criteria (or use lambda)
'''
def votes_filter_bigger_than_one_million(x):
    return x['votes'].sum() > 1000000

print('filtering by criteria: ', df.groupby('state').filter(votes_filter_bigger_than_one_million))

# groupby two or more criteria (and sum votes)
print('Group by State (abbreviation), candidates and sum their votes in each State: ', \
    df.groupby(['state_abbreviation', 'candidate'])['votes'].sum())
