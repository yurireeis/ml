import pandas as pd
import pydataset

titanic = pydataset.data('titanic')

# look for the columns
print('titanic dataset columns: ', titanic.columns)

# given a look on cathegoric data
print('titanic classes categoric data: ', titanic['class'].describe())

# look for how much memory the class is taken
print('how many memory titanic classes column is taken: ', titanic['class'].nbytes)

# truncate column to categoric type (better performance)
titanic_class = titanic['class'].astype('category')
print('titanic class truncated to category: ', titanic_class.describe())

# memory performance of trucated titanic class (to category)
print('how many memory titanic cathegoric class is taken: ', titanic_class.nbytes)
