'''
carregando arquivos do excel ou csv para ler este arquivo
'''
import pandas as pd

estoque = pd.read_csv('dataset/estoque.csv', delimiter=',')

# lendo as cinco primeiras linhas
print(estoque.head())
