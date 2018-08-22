import numpy as np

values = np.genfromtxt('./dataset/estoque.csv', delimiter=',', skip_header=1)
print(values)
