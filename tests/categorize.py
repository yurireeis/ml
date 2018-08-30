import pandas as pd
import numpy as np
import re
from unidecode import unidecode
from difflib import SequenceMatcher

df = pd.read_csv('dataset/estoque.csv')

# CASE 1: IF STRING HAS ONE POSITION ONLY, VALUE OF MODELO COLUMN MUST BE "NÃO INFORMADO"

def segregate_name(description):
    name = description
    words = unidecode(description).upper().split()
    has_more_than_one_word = (len(words) > 1)

    if not has_more_than_one_word: return name

    regex = re.compile(r'([0-9])', re.I)

    has_some_model_evidence = list(filter(regex.search, words))

    if has_some_model_evidence:
        del words[words.index(has_some_model_evidence[0]):]

    name = ' '.join(words)
    return name

def segregate_model(description):
    model_name = unidecode('Não informado').upper()
    words = unidecode(description).upper().split()
    has_more_than_one_word = (len(words) > 1)

    if not has_more_than_one_word: return model_name

    regex = re.compile(r'([0-9])', re.I)

    has_some_model_evidence = list(filter(regex.search, words))

    if not has_some_model_evidence: return model_name

    del words[:words.index(has_some_model_evidence[0])]

    model_name = ' '.join(words)
    return model_name

def is_acceptable_similar(name):
    for i, comp_name in enumerable(df['names']):
        sequence = SequenceMatcher(None, text, comp)
        longest_match = sequence.find_longest_match(0, len(name), 0, len(comp_name))
        percent = (longest_match.size / len(text)) * 100
        return (percent >= affordable_rate)

df['nomes'] = df['Descricao'].apply(segregate_name)
df['modelos'] = df['Descricao'].apply(segregate_model)
df['test'] = df['nomes'].apply(is_acceptable_similar)

similars = 0
differs = 0

# print(df.head())

print('total', len(df))
print('similars: ', similars)
print('differs: ', differs)
# # # group by name
# df_grouped_by_name = df.groupby('nomes')['modelos'].sum()
df.to_csv('result.csv')
