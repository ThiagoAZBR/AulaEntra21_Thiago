#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
'''                                         Continuação de Funções                                                  '''
# Testes para o "Projeto"


escolha = ""
while escolha != 'S' and escolha != 's':
    nome = input('Digite o primeiro nome:\n R: ')
    sobrenome = input('Digite o sobrenome:\n R: ')
    idade = int(input('Digite a idade:\n R: '))
    print(20 * '-=' + '-', 'Cadastro Terminado', 20 * '-=' + '-') # Adicionei esse print
    escolha = input("Deseja sair?(S/N) \n R: ") # Adicionei um espaço pra resposta

from Cadastrar_pessoas import nome_lista
from Cadastrar_pessoas import sobrenome_lista
from Cadastrar_pessoas import idade_lista

from Cadastrar_pessoas import cadastrar

from dadospessoais import number
from dadospessoais import adicionar_texto_pessoas
from dadospessoais import ler_texto_pessoas

cadastrar(nome, sobrenome, idade)
print(f"Os ID's Começam Em 1") # Adicionei Aqui para ver as opções à digitar
ide = int(input('Digite o id desejado: '))

adicionar_texto_pessoas()
ler_texto_pessoas(ide)
