#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#       a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#           id da pessoa
'''                                         Continuação de Funções                                                  '''
# Testes para o "Projeto"

from ex10 import cadastro
from function_ex12 import retorna_endereco_id

print('\n', 20 * '-=' + '-', 'Encontrar Endereços', 20 * '-=' + '-\n')


retorno_endereço = int(input('Digite O ID Mostrado Anteriormente: '))

retorna_endereco_id(retorno_endereço)



    