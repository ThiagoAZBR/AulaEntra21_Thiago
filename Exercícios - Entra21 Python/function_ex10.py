#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
'''                                         Continuação de Funções                                                  '''
lista_rua = []
lista_numero = []
lista_complemento = []
lista_bairro = []
lista_cidade = []
lista_estado = []
from Cadastrar import cadastro

# Testes para o "Projeto"

def cadastro_de_endereco(rua, numero, complemento, bairro, cidade, estado):
    lista_rua.append(rua)

    lista_numero.append(numero)

    lista_complemento.append(complemento)

    lista_bairro.append(bairro)

    lista_cidade.append(cidade)

    lista_estado.append(estado)

    if rua == '' or numero == '' or complemento == '' or bairro == '' or cidade == '' or estado == '':
        print('\n', 20 * '-=' + '-', 'O Cadastro Não Pôde Ser Feito Por falta de Dados.', 20 * '-=' + '-')
    else: 
        print('\n', 20 * '-=' + '-', 'Todos Os Dados Foram Preenchidos, Cadastro Concuído.', 20 * '-=' + '-')


    
