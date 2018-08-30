import pandas as pd
import numpy as np

'''
pivot table: sumarize your data by some criteria
'''

df = pd.read_csv('dataset/primary_results.csv')

# getting unique values in some series
print('Unique candidate values: ', df['candidate'].unique())

'''
What's happening here?
Index: the manner that I want to see the results (criteria)
Values: by the defined indexes, I wanna show the results by specific values
AggFunc: settled how the votes are presented (in this case, a sum is made)
'''
pivot_table = pd.pivot_table(
    df, index=['state', 'party', 'candidate'],
    values=['votes'],
    aggfunc={'votes': np.sum}
)

print('Pivot table: ', pivot_table)

'''
creating a rank column by country and party grouping by votes
(groupby object has the rank function available)
'''
df['rank'] = df.groupby(['county', 'party'])['votes'].rank(ascending=False)
print('Ranking by number of votes', df.head())

# I wanna know the ranking In an specific county
print('Los Angeles ranking is: ', df[df['county'] == 'Los Angeles'])

df_groupby = df.groupby(['state', 'party', 'candidate']).sum()

del df_groupby['fips'] # this value will be not used
del df_groupby['fraction_votes'] # this value will be not used

# re setting the indexes
df_groupby.reset_index(inplace=True)

print('Candidates with better rank by State, party and number of votes: ', df_groupby.head(10))

# grab rank by groupby object looking for state, party, and values as votes
df_groupby['rank'] = df_groupby.groupby(['state', 'party'])['votes'].rank(ascending=False)

print('Showing the first seven candidates by state: ', df_groupby.head(7))

'''
finally we will create the pivot table
'''
pivot_table_2 = pd.pivot_table(
    df_groupby,
    index=['state', 'party', 'candidate'],
    values=['rank', 'votes']
)

print('Definitive top 5 is: ', pivot_table_2.head(5))

# verify reincident first place terms in a dataset
print('The winner by party in most of the states is: ', \
    df_groupby[df_groupby['rank'] == 1]['candidate'].value_counts())
