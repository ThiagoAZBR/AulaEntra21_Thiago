lista_rua = []
lista_numero = []
lista_complemento = []
lista_bairro = []
lista_cidade = []
lista_estado = []
from Cadastrar_pessoas import cadastro
def cadastro_de_endereco(cont, rua, numero, complemento, bairro, cidade, estado):
    if cont < 0:
        pass
    else:
        if rua == '' or numero == '' or complemento == '' or bairro == '' or cidade == '' or estado == '':
            print('\n', 20 * '-=' + '-', 'O Cadastro Não Pôde Ser Feito Por falta de Dados.', 20 * '-=' + '-')
        else: 
            lista_rua.append(rua)
            cadastro['rua'] = lista_rua

            lista_numero.append(numero)
            cadastro['numero'] = lista_numero

            lista_complemento.append(complemento)
            cadastro['complemento'] = lista_complemento

            lista_bairro.append(bairro)
            cadastro['bairro'] = lista_bairro

            lista_cidade.append(cidade)
            cadastro['cidade'] = lista_cidade

            lista_estado.append(estado)
            cadastro['estado'] = lista_estado

            print('\n', 20 * '-=' + '-', 'Todos Os Dados Foram Preenchidos, Cadastro Concuído.', 20 * '-=' + '-')
            return 1
