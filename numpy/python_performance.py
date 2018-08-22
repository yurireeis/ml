from datetime import datetime

sum = 0
start = datetime.now()

for n in range(1, 100000001):
    sum += n

stop = datetime.now()
diff = stop - start

print('Result is {}. Ran in {} microseconds'.format(sum, diff.microseconds))
