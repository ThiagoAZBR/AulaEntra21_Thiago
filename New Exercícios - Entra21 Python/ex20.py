# 18 - 11

import sqlite3

conection = sqlite3.connect('Veiculo3_0.db')

cursor = conection.cursor()

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN marca TEXT;
''') # 1

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN modelo TEXT;
''') # 2

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN ano TEXT;
''') # 3

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN placa TEXT;
''') # 4

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN proprietario TEXT;
''') # 5

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN cor TEXT;
''') # 6

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN km_rodado TEXT;
''') # 7


cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN motor TEXT;
''') # 8

cursor.execute('''
ALTER TABLE veiculos
ADD COLUMN combustivel TEXT;
''') # 9

conection.commit()

print('Foi!')

conection.close()