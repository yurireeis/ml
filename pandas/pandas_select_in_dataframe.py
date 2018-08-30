'''
realizando seleção em um dataframe
'''
import pandas as pd

estoque = pd.read_csv('dataset/estoque.csv', delimiter=',')

# selecionando as colunas
print('dataframe columns selection: ', estoque.columns)

# descrevendo uma série de dados de um dataframe
print('describe a serie of a dataset: ', estoque['Descricao'].describe())
