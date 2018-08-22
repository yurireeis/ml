import matplotlib.pyplot as plt
import numpy as np

salary_marcos = np.array([100, 200, 400, 300])
salary_gileno = np.array([50, 300, 500, 450])
salary_pedro = np.array([200, 250, 300, 700])

fig = plt.figure()
plt.plot(salary_marcos, c='blue', ls='--', marker='s', ms='8', label='Salários Marcos')
plt.plot(salary_gileno, c='red', ls='--', marker='^', ms='8', label='Salários Gileno')
plt.plot(salary_pedro, c='green', ls='--', marker='o', ms='10', label='Salários Pedro')
plt.legend(loc='upper right')
fig.savefig('test_2.png')
