#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#       a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#           id da pessoa
'''                                         Continuação de Funções                                                  '''
# Testes para o "Projeto"

from ex10 import cadastro
def retorna_endereco_id(ide):
    print(f'''
        Rua: {cadastro['rua'][ide]}
        Número: {cadastro['numero'][ide]}
        Complemento: {cadastro['complemento'][ide]}
        Bairro: {cadastro['bairro'][ide]}
        Cidade: {cadastro['cidade'][ide]}
        Estado: {cadastro['estado'][ide]}''')