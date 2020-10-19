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

print('\nO Primeiro ID é 1')
ide = int(input('Digite Um ID: \n R: '))


from function_ex10 import lista_rua
from function_ex10 import lista_numero
from function_ex10 import lista_complemento
from function_ex10 import lista_bairro
from function_ex10 import lista_cidade
from function_ex10 import lista_estado  # Capta Os Dados

from function_ex10 import cadastro_de_endereco # Função Que Armazena em Lista
from dadosendereco import number # O Número A Ser verificado pela ultima Função: ler_texto_endereco
from dadosendereco import adicionar_texto_endereco # A Função Que joga para o Arquivo os Dados  
from dadosendereco import ler_texto_endereco # A Função Le o Arquivo E Mostra o Resultado

cadastro_de_endereco(rua, numero_casa, complemento, bairro, cidade, estado)
adicionar_texto_endereco()
ler_texto_endereco(ide)

