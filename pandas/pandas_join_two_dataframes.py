import pandas as pd
from db import DemoDB

database = DemoDB()

print('database tables: ', database.tables)

album = database.tables.Album.all()
artist = database.tables.Artist.all()

print('artist: ', artist)

'''
joining album info + artist info
it's not magical... in this case, pandas only look foward for columns with the
same name
'''
album_artist = pd.merge(artist, album)
print('album and artist info sample: ', album_artist.head())

'''
you can set (as you wish) the name of the column that has to merge
'''
album_artist = pd.merge(artist, album, on='ArtistId')
print('album and artist info set "on column" information: ', album_artist.head())

# rename a column name
album.rename(columns={'ArtistId': 'Artist_Id'}, inplace=True)

# making a merge with two distincts column names
album_artist = pd.merge(album, artist, left_on='Artist_Id', right_on='ArtistId')
print('album and artist set correspondent columns info: ', album_artist.head())

# droping duplicated column
album_artist = pd.merge(album, artist, left_on='Artist_Id', right_on='ArtistId').drop('Artist_Id', axis=1)
print('album and artist set correspondent columns info: ', album_artist.head())

# merging by name
students_1 = pd.DataFrame({
    'name': ['Maria', 'Sofia'],
    'grade': [8, 9]
})

students_2 = pd.DataFrame({
    'name': ['João', 'Pedro', 'Maria'],
    'code': [1, 2, 3]
})

all_students_inner = pd.merge(students_1, students_2)

'''
when you did a simple merge like this, only data present in both cases
are find by a result (intersection) (inner)
'''
print('listing students considering common (inner) values: ', all_students_inner.head())

'''
merge considering all results, and fill non-coincident values with NaN (outer)
'''
all_students_outer = pd.merge(students_1, students_2, how='outer')
print('listing students considering outer values: ', all_students_outer.head())

'''
merge considering left values, and fill non-coincident values with NaN (left)
'''
all_students_left = pd.merge(students_1, students_2, how='left')
print('listing students considering left values: ', all_students_left.head())

'''
merge considering right values, and fill non-coincident values with NaN (right)
'''
all_students_right = pd.merge(students_1, students_2, how='right')
print('listing students considering right values: ', all_students_right.head())
