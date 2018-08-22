import numpy as np

'''
na matriz, as listas são consideradas as linhas e os valores de cada lista
interna são consideradas as colunas
'''

# matriz quadrada
print(np.array([[1, 2], [3, 4]]))

# matriz identidade (elementos diagonais são 1 e o restante zero)
print('identity matrix', np.array([[1, 0], [0, 1]]))


joao_pts = [20, 30, 40, 15]
pedro_pts = [100, 24, 48, 23]
maria_pts = [92, 22, 34, 12]
marcos_pts = [12,34,12,43]

pontos = np.array([joao_pts, pedro_pts, maria_pts, marcos_pts])

print('points: ', pontos)

# pontos do joao
print('john points: ', pontos[0])

# criando um array com valores uniformemente espaçados
my_data = np.arrange(0, 20)

# transformando um array em uma ordem desejada (ex.: 5 linhas e 4 colunas)
reshaped_matrix = np.reshape(my_data, (5, 4))

# pegando um elemento pelo índice de forma absoluta
pontos.item(5)

'''
operações com matrizes
'''
matrix1 = np.array([np.arrange(0, 3), np.arrange(3, 6)])
matrix2 = np.array([np.arrange(6, 9), np.arrange(9, 12)])

# divindo
result = matrix1 / matrix2

# divindo com arredondamento
result2 = np.matrix.round(matrix1 / matrix2)

# multiplicando/somando/subtraindo/potencializando os valores da matriz
result3 = matrix1 ** 1
result4 = matrix1 * 1
result5 = matrix1 + 1
result6 = matrix1 - 1
