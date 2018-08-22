import matplotlib.pyplot as plt
import numpy as np

salary = np.array([100, 200, 300, 500, 400, 150])

salary *= 2

fig = plt.figure()
plt.plot(salary, c='blue', ls='--', marker='s', ms='18')
fig.savefig('test.png')
