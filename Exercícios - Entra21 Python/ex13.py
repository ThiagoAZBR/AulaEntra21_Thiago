#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#               com seus respectivos endereços utilizando as funções do ex3 e ex4
'''                                         Continuação de Funções                                                  '''
# Testes para o "Projeto"
# (Atualizando) Teste BEM SUCEDIDO!

###################################### Início dos Imports  ##########################################################

from Cadastrar_pessoas import nome_lista
from Cadastrar_pessoas import sobrenome_lista
from Cadastrar_pessoas import idade_lista # Capta os Dados

from function_ex10 import lista_rua
from function_ex10 import lista_numero
from function_ex10 import lista_complemento
from function_ex10 import lista_bairro
from function_ex10 import lista_cidade
from function_ex10 import lista_estado  # Capta Os Dados

from Cadastrar_pessoas import cadastrar # Função Que Armazena em Lista

from function_ex10 import cadastro_de_endereco # Função Que Armazena em Lista

from dadosendereco import adicionar_texto_endereco # A Função Que joga para o Arquivo os Dados  
from dadosendereco import ler_texto_endereco # A Função Le o Arquivo E Mostra o Resultado

from dadospessoais import number
from dadospessoais import adicionar_texto_pessoas # A Função Que joga para o Arquivo os Dados
from dadospessoais import ler_texto_pessoas # A Função Le o Arquivo E Mostra o Resultado

######################################### FIM DOS IMPORTS #########################################################



###################################### Adquirindo os Dados ###################################################

escolha = ""
while escolha != 'S' and escolha != 's':
    nome = input('Digite o primeiro nome:\n R: ')
    sobrenome = input('Digite o sobrenome:\n R: ')
    idade = int(input('Digite a idade:\n R: '))
    print(20 * '-=' + '-', 'Cadastro Terminado', 20 * '-=' + '-') # Adicionei esse print
    escolha = input("Deseja sair?(S/N) \n R: ") # Adicionei um espaço pra resposta

cadastrar(nome, sobrenome, idade) # Caso Seja insuficiente a Idade, só vai reiniciar o cadastro Aqui

print(20 * '-=' + '-', 'Cadastro de Endereço', 20 * '-=' + '-\n')

rua = input('Nome da Rua: ')
numero_casa = input('Numero da Residência: ')
complemento = input('Complemento: ')
bairro = input('Bairo: ')
cidade = input('Cidade: ')
estado = input('Estado: ')

###################################### Dados Adquiridos ######################################################


cadastro_de_endereco(rua, numero_casa, complemento, bairro, cidade, estado)


print(f"Os ID's Começam Em 1") 
arquivo = open('DadosPessoas.txt', 'r')
linhas = len(arquivo.readlines())
print("O Total de ID's Até agora é", linhas + 1) # Adicionei Aqui para ver as opções à digitar
arquivo.close()

ide = int(input('Digite o id desejado: '))

adicionar_texto_pessoas()
adicionar_texto_endereco()

ler_texto_pessoas(ide)
ler_texto_endereco(ide)

################################################  FIM  ################################################################