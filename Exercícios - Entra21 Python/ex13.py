#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#               com seus respectivos endereços utilizando as funções do ex3 e ex4
'''                                         Continuação de Funções                                                  '''
# Testes para o "Projeto"

from ex09 import cadastro
from ex10 import cadastro
from ex09 import ide
from function_ex12 import retorna_endereco_id
from Listar import retorna_pessoa_id

ide = int(input('\nDigite o ID Para Ver Os Dados: \n (O ID que foi dado Anteriormente Serve) \n R: '))

retorna_pessoa_id(ide)

retorna_endereco_id(ide)

