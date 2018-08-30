'''
datasets de domínio público que podem facilmente ser utilizados
já vem em formato de datafram no pandas
'''
import pandas as pd
import pydataset

# lista todos os bancos de dados que eles tem disponíveis
print('available datasets: ', pydataset.data())

# armazenando o dataset do titanic
titanic_dataframe = pydataset.data('titanic')

# pegando os cinco primeiros valores
print('titanic first results: ', titanic_dataframe.head())

# realizando um describe do dataframe do titanic
print('titanic dataframe info: ', titanic_dataframe.describe())

# realizando um count simples da série class do titanic
print('titanic passengers class info: ', titanic_dataframe['class'].value_counts())
