from pessoas import Pessoa    


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
    senha = input('\nSua Senha de 6 Dígitos: ')
    letras_secretas = input('\nQuais Seriam As Letras Secretas?\nR: ')
    
    file = open('pessoas.txt', 'a')
    file.write((f'{pergunta_secreta};{resposta};{senha};{letras_secretas}\n'))
    file.close()
    