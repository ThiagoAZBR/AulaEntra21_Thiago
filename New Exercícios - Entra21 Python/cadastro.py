from pessoas import Pessoa    
from dados import contar

'''
def cadastrar_pessoa():
    nome = input("Nome: ")
    data_nasc = input("Data: ")
    cpf = input("Cpf")
    telefone = input("Tel")
    email = input("Email:")
    endereco = input("Endereco: ")
    p1 = Pessoa(id(nome), nome, cpf, email, endereco, data_nasc, telefone)
    salvar_arquivo(p1)
    # return p1   | Alterado

def salvar_arquivo(pessoa):
    file = open("pessoas.txt", "a")
    file.write(f"{pessoa.id};{pessoa.nome};{pessoa.data_nasc};{pessoa.cpf};{pessoa.telefone};{pessoa.email};{pessoa.endereco};{pergunta_secreta};{resposta};{senha};{letras_secretas}")
    file.close()

def cadastrar_conta(pessoa):
    pergunta_secreta = input('Qual Pergunta Secreta Deseja Ter?\nR: ')
    resposta = input('\nE Qual Seria A Resposta?\nR: ')
    senha = input('\nSua Senha de 7 Dígitos: ')
    letras_secretas = input('\nQuais Seriam As Letras Secretas?\nR: ')
    
    file = open('pessoas.txt', 'a')
    file.write((f'{pergunta_secreta};{resposta};{senha};{letras_secretas}\n'))
    file.close()
 '''   
from pessoas import Pessoa, Conta_Banco
from saque import saque
from deposito import fazer_deposito
from random import randint
from dados import visualizar_dados

def cadastrar_pessoa():
    nome = input("Nome: ")
    cpf = input('CPF: ')
    data_nasc = input("Data de Nascimento: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    endereco = input("Endereço: ")
    pessoa = Pessoa(nome, cpf, email, endereco, data_nasc, telefone)
    salvar_arquivo(pessoa)
    return pessoa
    return cpf

def procurar_cpf (cpf):
    lista_cpfs = []
    #criando lista com os cpfs já cadastrados
    with open("pessoas.txt", "r") as file:
        for linha in file.readlines():
            lista_cpfs = linha.split(";")[0]

    #verificando se o cpf já costa nos registros
    if cpf in lista_cpfs:
        return False
    return True

def salvar_arquivo(pessoa):
    with open("pessoas.txt", "a") as file:
        file.write(f"{pessoa.cpf};{pessoa.nome};{pessoa.data_nasc};{pessoa.telefone};{pessoa.email};{pessoa.endereco}\n")
        file.close()

def cadastrar_conta(option_bank, cpf):
    # Vai Começar a Criar as Senhas!
    pergunta_secreta = input('Qual Pergunta Secreta Deseja Ter?\nR: ').strip()
    resposta = input('\nE Qual Seria A Resposta?\nR: ').strip()
    senha = input('\nSua Senha de 7 Caractéres: ').strip()
    
    quant = len(senha) # Vai Verificar A Quantidade de caracteres
    while quant != 7:
        print('\nERRO! Precisa Ser Exatamente 7 Caractéres!')
        senha = input('\nSua Senha de 7 Caractéres: ').strip() # Acabou A Verificação
        quant = len(senha)
    letras_secretas = input('\nQuais Seriam As Letras Secretas?\nR: ').strip().upper()
    numconta = ''
    print(f'Seu Número Da Conta é: {id(numconta)}\nAnote Para Não Esquecer!!!\n')
    agencia = randint(1,9)
    agencia = str(agencia)
    numconta = id(numconta)
    numconta = str(numconta)
    # Vai Enviar Para o Arquivo txt
    conta1 = Conta_Banco(cpf, numconta, pergunta_secreta, resposta, senha, letras_secretas)

    file = open('conta.txt', 'a')
    file.write(f'{option_bank};{conta1.cpf};{agencia};{conta1.numconta};{conta1.senha};{conta1.pergunta_secreta};{conta1.resposta};{conta1.letras_secretas}\n')
    file.close()


def acessar_conta(): # Problema Encontrado Aqui, as informações teriam que ser pedidas antes do loop
    numero_conta = input("Informe o número da conta: ")
    senha = input("Informe a senha: ")
    letra = input("Informe a senha de letra: ")
    quant = ''
    while True:
                # Elas estavam sendo pedidas aqui, então quando voltava as opçoes pedia tudo de novo

        option = int(input(f'''
        1 - Visualizar Saldo
        2 - Fazer um depósito #Eduarda
        3 - Saque
        4 - Transferência
        5 - Visualizar Dados
        6 - Sair\n\nR: '''))

        if option == 1:
            visualizar_saldo(numero_conta)
        elif option == 2:
            fazer_deposito(numero_conta)
        elif option == 3:
            saque(numero_conta)
        elif option == 4:
            pass
            #fazer_transferencia(numero_conta)
        elif option == 5:
            contar()
            visualizar_dados(numero_conta, quant)
            print('certo?')
        else:
            break


def visualizar_saldo(numero_conta):
    file = open("conta.txt", "r")
    for procura in file: 
        linha = procura.strip()
        lista_conta = linha.split(";")
        if numero_conta == lista_conta[3]:
            print(f"Seu saldo é: {lista_conta[5]}")
    file.close()