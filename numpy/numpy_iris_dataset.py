import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('./dataset/iris.data', delimiter=',', usecols=(0,1,2,3), skip_header=0)

# quantidade de elementos do dataset
print('dataset quantity: ', len(data))

# mostrando apenas os resultados do primeiro atributo (comprimento da sépala)
print('all sepal length (in cm) elements', data[:, 0])

# mostrando apenas os dez primeiros resultados do primeiro atributo (comprimento da sépala)
print('first ten results of sepal length (in cm) elements', data[:10, 0])

'''
plotando (comprimento da sépala)
o primeiro parâmetro passado ao data representa o valor de onde irá partir e
o valor superior máximo
'''
fig = plt.figure()
plt.plot(data[:50, 0], c='red', ls=':', marker='o', ms=5, label='Íris-Setosa')
plt.plot(data[51:100, 0], c='blue', ls=':', marker='^', ms=5, label='Íris-Versicolor')
plt.legend(loc='upper right')
fig.savefig('test_3.png')
