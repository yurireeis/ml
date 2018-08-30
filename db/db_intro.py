'''
usado para quando queremos trazer para a mémoria informações do banco
e trabalhar o dataframe
'''
from db import DB
from mssql import conn

db = conn()

c = db.cursor()
c.execute ('select foo from bar')
rs = c.fetchall()
# for r in rs:
#     print r[0]
