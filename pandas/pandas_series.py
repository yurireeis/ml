import pandas as pd
import numpy as np

# irá imprimir o índice e o valor correspondente ao índice da série
serie = pd.Series(np.arange(0, 10))
print('my first one dimension array (serie): ', serie)

# describe irá mostrar o valor máximo, mínimo, desvio padrão, mediana, etc
print('info about the serie: ', serie.describe())

# mostrando a média
print('mean: ', serie.mean())

# mostrando a mediana
print('median: ', serie.median())

# mostra onde os valores estão duplicados em uma série
print('show how index has duplicated values: ', serie.duplicated())

# adicionando uma série a outra
serie2 = pd.Series(np.arange(7, 14))
serie2 = serie2.append(serie)
print('append serie to serie 2: ', serie2)

# com valores duplicados, verifica novamente se há ou não na serie2
print('show how index has duplicated values: ', serie2.duplicated())
