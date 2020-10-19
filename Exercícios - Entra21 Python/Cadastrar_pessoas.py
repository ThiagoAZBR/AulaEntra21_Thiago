cadastro = {}
nome_lista = []
sobrenome_lista = []
idade_lista = []

def cadastrar(nome, sobrenome, idade):

    if idade >= 18:

        nome_lista.append(nome)

        sobrenome_lista.append(sobrenome)

        idade = str(idade)
        idade_lista.append(idade)

        

    else:
        print('\nIdade insuficiente!\n')
        print('Refaça O Cadastro!\n')
        escolha = ""
        while escolha != 'S' and escolha != 's':
            nome = input('Digite o primeiro nome:\n R: ')
            sobrenome = input('Digite o sobrenome:\n R: ')
            idade = int(input('Digite a idade:\n R: '))
            print(20 * '-=' + '-', 'Cadastro Terminado', 20 * '-=' + '-') # Adicionei esse print
            escolha = input("Deseja sair?(S/N) \n R: ") # Adicionei um espaço pra resposta
