from Cadastrar_pessoas import cadastro, cadastrar
from Listar_pessoas import retorna_pessoas, retorna_pessoa_id
from Cadastrar_enderecos import cadastro_de_endereco
from Listar_enderecos import retorna_enderecos, retorna_endereco_id
#                               Atividade Em Dupla Robinson e Thiago

'''                                         Continuação de Funções                                                  '''

cont = 0
escolha = ''
i = 0
while escolha != '6':
    print('''
    1 - Cadastrar
    2 - Consultar todos os dados
    3 - Consultar dados por id
    4 - Consultar todos os endereços
    5 - Consultar todos os Nomes e Idades
    6 - Sair
    ''')
    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        nome = input('Digite um nome: ')
        sobrenome = input('Digite um sobrenome: ')
        idade = int(input('Digite uma idade: '))
        cont = cadastrar(nome, sobrenome, idade, cont)
        
        if cont >= 0:
            while i != 1:
                rua = input('Digite uma rua: ')
                numero = input('Digite um número: ')
                complemento = input('Digite um complemento: ')
                bairro = input('Digite um bairro: ')
                cidade = input('Digite uma cidade: ')
                estado = input('Digite um estado: ')
                i = cadastro_de_endereco(cont, rua, numero, complemento, bairro, cidade, estado)
        else:
            cont = cont * -1

    elif escolha == '2':
        tam = len(cadastro['ide'])
        for i in range(tam):
            retorna_pessoa_id(i)
            retorna_endereco_id(i)
    
    elif escolha == '3':
        ide = int(input('\nDigite o id desejado: '))
        retorna_pessoa_id(ide)
        retorna_endereco_id(ide)

    elif escolha == '4':
        retorna_enderecos()

    elif escolha == '5':
        retorna_pessoas()

    elif escolha == '6':
        print('\nAdeus!')
    
    else:
        print('\nEscolha inválida!')
