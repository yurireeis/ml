import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''
linspace create an array to work with data. The first and second values is
the range and the third value is the quantity of elements
'''
random_serie = np.linspace(1, 10, 100)

fig = plt.figure()
plt.plot(random_serie, np.sin(random_serie), c='blue', ls='--', marker='s', ms='8', label='Random Serie')
plt.legend(loc='upper right')
fig.savefig('test_4.png')
