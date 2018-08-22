import pandas as pd

'''
recebe uma lista de listas
basicamente recebe várias séries

primeiro argumento do dataframe: dados em si
segundo argumento do dataframe: nome das séries
'''
df = pd.DataFrame([
    ['fchollet/keras', 11302],
    ['openai/universe', 4350],
    ['pandas/dev/pandas', 8168]
], columns=['repository', 'stars'])

# verificar qual é a dimensão do dataframe (neste caso três linhas e duas colunas)
print('total numbers of lines/colums: ', df.shape)

'''
para acessar, quando definidas as colunas, deverá ser repassado no índice o
nome da série.
'''
print('accessing the repository series: ', df['repository'])

'''
calculando a média (por exemplo) de uma das séries de dados
'''
print('mean of stars: ', df['stars'].mean())

'''
calculando a mediana (por exemplo) de uma das séries de dados
'''
print('mean of stars: ', df['stars'].median())

'''
caso queira especificamente uma linha (sem chamar pelo nome da série),
utilizar o método iloc
'''
print('repository by line number: ', df.iloc[0])
