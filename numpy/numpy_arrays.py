import numpy as np

# criando um array np
a = np.array([20, 30 , 40, 50])
print('np array: ', a)

# iniciar a partir do 1 e o três é o index do limite superior aberto
print('starting from index 1 and set open superior limit as 3: ', a[1:3])

# setando passos
print('no limits with two steps: ', a[::2])

# criando uma cópia
b = a.copy()

# inserindo elementos no array (ex.: [1, 10, 2 , 3])
arr = [1, 2, 3]
np.insert(arr, 1, 10)

'''
os eixos são definidos para elementos multidimensionais
caso você não defina um eixo, ele vai planificar os arrays
'''

# somando o primeiro eixo (vertical) (ex.: [4, 6])
axis_y = np.array([[1, 2], [3, 4]]).sum(axis=0)

# somando o segundo eixo (horizontal) (ex.: [3, 7])
axis_x = np.array([[1, 2], [3, 4]]).sum(axis=1)

# anexando valores no final (append)
a = np.array([1, 2, 3])
np.append(a, [4, 5, 6])
