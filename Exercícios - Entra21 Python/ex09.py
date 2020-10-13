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

from Cadastrar import cadastro, cadastrar
from Listar import retorna_pessoas, retorna_pessoa_id
cont = 0
escolha = ""
while escolha != 'S'and escolha != 's':
    ide = 0
    nome = input('Digite um nome: ')
    sobrenome = input('Digite um sobrenome: ')
    idade = int(input('Digite uma idade: '))
    print(20 * '-=' + '-', 'Cadastro Terminado', 20 * '-=' + '-') # Adicionei esse print
    escolha = input("Deseja sair?(S/N) \n R: ") # Adicionei um espaço pra resposta
    cont = cadastrar(nome, sobrenome, idade, cont)
    cont = cont + 1
print(f'Opções De ID a Digitar: {ide}') # Adicionei Aqui para ver as opções à digitar
ide = int(input('Digite o id desejado: '))
retorna_pessoa_id(ide)

