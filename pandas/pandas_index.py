import pandas as pd

df = pd.DataFrame([
    ['PE', 'Pernambuco', 'Recife'],
    ['SC', 'Santa Catarina', 'Florianópolis'],
    ['SP', 'São Paulo', 'São Paulo']
], columns=['Sigla', 'Nome', 'Capital'])

'''
para verificar a forma de indexação, basta utilizar a propriedade index, tanto
na série quanto no DataFrame
'''
print('index config of DataFrame: ', df.index)

'''
acessando a linha que está com o índice 0
a diferença que ix trata especificamente de índice, que nem sempre será
numérico. Diferente de iloc que é a posição em si.
'''
print('index 0 line is: ', df.ix[0])

'''
o código abaixo mostra como alterar o valor do índice
'''
df.index = pd.Index(['x', 'y', 'z'])
print('new index is: ', df)

'''
alterando o valor do índice para uma determinada série de dados
'''
df.index = df['Sigla']
print('new index is: ', df)
