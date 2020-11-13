from pessoas import Pessoa, Conta_Banco
from cadastro import cadastrar_conta, cadastrar_pessoa, acessar_conta, salvar_arquivo
from random import randint

cpf = ''

class Banco():
    def __init__(self):
        #lista bancos nome ai a pessoa só passa a opção
        self.nome = nome
    def cadastrar_pessoa(self):
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
    def cadastrar_conta(self,bank, cpf):
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
        file.write(f'{bank};{conta1.cpf};{agencia};{conta1.numconta};{conta1.senha};{conta1.pergunta_secreta};{conta1.resposta};{conta1.letras_secretas}\n')
        file.close()

class NuConta(Banco):
    def __init__(self ):
        super().__init__()

class Viacredi(Banco):
    def __init__(self):
        super().__init__()

class Bradesco(Banco):
    def __init__(self):
        super().__init__()

class Itau(Banco):
    def __init__(self):
        super().__init__()

class BancoInter(Banco):
    def __init__(self):
        super().__init__()

class Safra(Banco):
    def __init__(self):
        super().__init__()

class Conta(Banco):
    def __init__(self, banco:Banco, pessoa:Pessoa, numero:str, agencia:str, tipo_conta:int, saldo:float, senha:str):
        super().__init__(banco)
        self.pessoa = pessoa
        self.numero = numero
        self.agencia = agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.senha = senha

banco = [Viacredi, NuConta, Bradesco, Itau, BancoInter, Safra]



if __name__ == "__main__":
    while True:
        valor = int(input(
            """Digite a operação desejada: \n
    1 - Cadastrar Conta
    2 - Acessar Conta #senha, letra paara entra return numero, agencia
    3 - Sair\n
R: """))



        if valor == 1:
            option_bank = input('''
Qual Banco Deseja Se Cadastrar?
  (Digite O Número Da Opção)

1 - Viacredi            2 - NuConta            3 - Bradesco

4 - Itaú                5 - BancoInter         6 - Safra

R: ''')

        

            if option_bank == '1':
                option_bank = int(option_bank) - 1
                print(f'\nSeu Cadastramento para {banco[option_bank].__name__} irá Começar...\n')
                Viacredi.cadastrar_pessoa('')
                Viacredi.cadastrar_conta('', banco[option_bank].__name__, cpf)
                
                
            elif option_bank == '2':
                option_bank = int(option_bank) - 1
                print(f'\nSeu Cadastramento para {banco[option_bank].__name__} irá Começar...\n')
                NuConta.cadastrar_pessoa('')
                NuConta.cadastrar_conta('', banco[option_bank].__name__, cpf)

            elif option_bank == '3':
                option_bank = int(option_bank) - 1
                print(f'\nSeu Cadastramento para {banco[option_bank].__name__} irá Começar...\n')
                Bradesco.cadastrar_pessoa('')
                Bradesco.cadastrar_conta('', banco[option_bank].__name__, cpf)

            elif option_bank == '4':
                option_bank = int(option_bank) - 1
                print(f'\nSeu Cadastramento para {banco[option_bank].__name__} irá Começar...\n')
                Itau.cadastrar_pessoa('')
                Itau.cadastrar_conta('', banco[option_bank].__name__, cpf)

            elif option_bank == '5':
                option_bank = int(option_bank) - 1
                print(f'\nSeu Cadastramento para {banco[option_bank].__name__} irá Começar...\n')
                BancoInter.cadastrar_pessoa('')
                BancoInter.cadastrar_conta('', banco[option_bank].__name__, cpf)

            elif option_bank == '6':
                option_bank = int(option_bank) - 1
                print(f'\nSeu Cadastramento para {banco[option_bank].__name__} irá Começar...\n')
                Safra.cadastrar_pessoa('')
                Safra.cadastrar_conta('', banco[option_bank].__name__, cpf)                

                
            
                
            else:
                print(10 * '=', 'Você Digitou Incorretamente!', 10 * '=', '\n')

            
        elif valor == 2:
            acessar_conta()
        elif valor == 3:
            print("Agradecemos a sua visita!")
            break
        else:
            print("Opção inválida!\n Tente novamente!")

# Consertar Erro na Hora de Coordenar a Visualização de Dados
# Ele não está verificando o certo
# Também não está enviando para o arquivo conta o cpf