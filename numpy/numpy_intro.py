import numpy

# listas do numpy consomem menos memória, o que faz toda a diferença para grande volume de dados
# são menos flexíveis do que as listas convencionais do python
# para a matemática científica são vitais
# para operações vetoriais e matriciais é muito útil

# recebe uma lista e transforma em um array ndarray
simple_array = numpy.array([10, 20, 30, 40])
print('simple array: ', simple_array)

# criando um array multidimensional (nesse caso são duas linhas e duas colunas)
multi_dimensional = numpy.array([[1, 2], [3, 4]])

# se deixar -1 é o última coluna, assim como também a última linha)
print('last line and last column: ', multi_dimensional[-1][-1])

# transposta transforma linhas em colunas
print('transpose (transform lines in colums): ', multi_dimensional.transpose())

# somando duas matrizes
# quantidade de linhas e colunas devem ser iguais
print('sum of the matrix is: ', numpy.array([[1, 2], [3, 4]]) + numpy.array([[5, 6], [7, 8]]))

# somando todos os argumentos de um array
print('the sum of the arguments is: ', numpy.array([1, 2, 3, 4]).sum())

# pegando o index do maior argumento
print('the position of the bigger argument is: ', numpy.array([1, 2, 3, 4]).argmax())

# pegando o index do menor argumento
print('the position of the smallest argument is: ', numpy.array([1, 2, 3, 4]).argmin())

# retorna a mediana dos valores
print('the mean of the values is: ', numpy.array([1, 2, 3, 4, 5]).mean())

# retorna os valores diagonais da matriz
print('the mean of the list is: ', multi_dimensional.diagonal())

# retorna a dimensão da matriz
print('the dimension of the matrix is: ', multi_dimensional.ndim)
