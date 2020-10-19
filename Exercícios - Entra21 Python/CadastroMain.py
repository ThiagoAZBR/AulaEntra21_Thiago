from dadospessoais_funcao_final import adicionar_texto_pessoas, ler_texto_pessoas
from dadosendereco_funcao_final import adicionar_texto_endereco, ler_texto_endereco, ler_todos_dados
escolha = ''
while escolha != '4':
    x = 0
    y = 0
    print('''
    1 - Cadastrar
    2 - Consultar todos os dados
    3 - Consultar dados por id
    4 - Sair
    ''')
    escolha = input('Digite sua escolha: ')

    if escolha == '1':
        while x != 1:
            nome = input('Digite um nome: ')
            sobrenome = input('Digite um sobrenome: ')
            idade = int(input('Digite uma idade: '))

            if idade < 18:
                print('Idade inválida! Cadastre novamente!')
            else:
                ide = adicionar_texto_pessoas(nome, sobrenome, idade)
                x = 1
        while y != 1:
            rua = input('Digite uma rua: ')
            numero = input('Digite um número: ')
            complemento = input('Digite um complemento: ')
            bairro = input('Digite um bairro: ') 
            cidade = input('Digite uma cidade: ')
            estado = input('Digite um estado: ')
            if rua == '' or numero == '' or complemento == '' or bairro == '' or cidade == '' or estado == '':
                print('Campo(s) vazio(s)! Cadastre novamente!')
            else:
                adicionar_texto_endereco(rua, numero, complemento, bairro, cidade, estado, ide)
                y = 1

    elif escolha == '2':
        ler_todos_dados()

    elif escolha == '3':
        ide = input('Digite o ID desejado: ')
        ler_texto_pessoas(ide)
        ler_texto_endereco(ide)

    elif escolha == '4':
        print('\nAdeus!')

    else:
        print('\nEscolha inválida!')
