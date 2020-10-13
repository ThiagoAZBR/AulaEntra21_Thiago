#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
'''                                         Continuação de Funções                                                  '''
# Testes para o "Projeto"

print(20 * '-=' + '-', 'Cadastro de Endereço', 20 * '-=' + '-\n')

rua = input('Nome da Rua: ')
numero_casa = input('Numero da Residência: ')
complemento = input('Complemento: ')
bairro = input('Bairo: ')
cidade = input('Cidade: ')
estado = input('Estado: ')


from function_ex10 import cadastro_de_endereco
from function_ex10 import cadastro

cadastro_de_endereco(rua, numero_casa, complemento, bairro, cidade, estado)


print(f'''
    Rua: {cadastro['rua'][0]}
    Número da Casa: {cadastro['numero'][0]}
    Complemento: {cadastro['complemento'][0]}
    Bairro: {cadastro['bairro'][0]}
    Cidade: {cadastro['cidade'][0]}
    Estado: {cadastro['estado'][0]}''')