import numpy
from datetime import datetime

start = datetime.now()
sum = numpy.arange(1, 100000001).sum()
stop = datetime.now()
diff = stop - start
elapsed_ms = (diff.days * 86400000) + (diff.seconds * 1000) + (diff.microseconds / 1000)

print('Result is {}. Ran in {} milliseconds'.format(sum, elapsed_ms))
