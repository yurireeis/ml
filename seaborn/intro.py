'''
seaborn changes the style of graphics
(runs with matplotlib)
'''
import matplotlib.pyplot as plt
import numpy as np

# change style of seaborn plot
# sns.set_style('white')

random_serie = np.linspace(1, 10, 100)

fig = plt.figure()

# plot two infos at the same time
import seaborn as sns
plt.plot(random_serie, np.sin(random_serie), 'b--')
plt.plot(random_serie, np.cos(random_serie), 'r--')
fig.savefig('test_5.png')
