# 17/11

import sqlite3
from datetime import datetime

conexao = sqlite3.connect('Veiculo3_0.db')

cursor = conexao.cursor()

#Já Criado

# cursor.execute('''
# CREATE TABLE veiculos (
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#     nome_veiculo TEXT NOT NULL,
#     rodas TEXT NOT NULL,
#     quant_de_pessoas TEXT NOT NULL,
#     portas TEXT NOT NULL,
#     onde_se_locomove TEXT NOT NULL,
#     criado_em DATE NOT NULL
# )
# ''')


# name = input('O Que é O Seu Veículo? \nR: ')
# wheel = input('Há Rodas?\nR: ').upper()

# if wheel == 'SIM' or wheel == 'S':
#     while True:
#         try:
#             quant_wheel = int(input('Quantas Rodas Tem? \nR: '))
#         except ValueError:
#             print('Escreva Novamente O Valor está incorreto!')
#         else:
#             break
# else:
#     quant_wheel = 0

# door = input('Há Portas?\nR: ').capitalize()

# local = input('Onde se Usa esse Veículo? ex: Terra, Água...\nR: ')



# tempo = datetime.now()
# tempo = tempo.strftime('%d - %m - %Y   %H:%M:%S')

# cursor.execute(f'''
# INSERT INTO veiculos (nome_veiculo, rodas, quant_de_pessoas, portas, onde_se_locomove, criado_em)
# VALUES ('{name}', '{wheel} Tem rodas', {quant_wheel}, '{door} Tem Portas', '{local}', '{tempo}')
# ''')

# conexao.commit()

# cursor.execute('''
# UPDATE veiculos
# SET marca = 'Adidas', modelo = '2.0', ano = '1998', placa = 'BRASIL - 55', proprietario = 'Silvio Santos', cor = 'Dourado', km_rodado = '0', motor = 'V8', combustivel = 'Diesel De Cana De Açucar'
# ''')



# conexao.execute('''
# UPDATE veiculos
# SET marca = 'AirBus'
# WHERE id = 1
# ''')

# conexao.commit()

cursor.execute('''
SELECT * FROM veiculos;
''')

for linha in cursor.fetchall():
    print(linha)

conexao.close()