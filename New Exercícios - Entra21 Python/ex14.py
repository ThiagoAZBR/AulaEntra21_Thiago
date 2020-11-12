from pessoas import Pessoa      
from time import sleep
from random import randint


# Alt = Alterado 
#from cadastro import salvar_arquivo #, cadastrar_pessoa,  cadastrar_conta 



class Banco:
    def __init__(self): # Alt
        pass

#    def salvar_arquivo(self, pessoa): # Alt


    def cadastrar_pessoa(self): # Alt
        nome = input("Nome: ")
        data_nasc = input("Data: ")
        cpf = input("Cpf: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        endereco = input("Endereco: ")

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
        print(f'Seu Número Da Conta é: {id(nome)}\nAnote Para Não Esquecer!!!')
        agencia = randint(1,9)
        agencia = str(agencia)
        # Vai Enviar Para o Arquivo txt
        p1 = Pessoa(id(nome), nome, cpf, email, endereco, data_nasc, telefone, pergunta_secreta, resposta, senha, letras_secretas)

        file = open("C:\\Users\\thiago.zeferino\\Desktop\\Thiago Augusto Zeferino\\[Programas]\\AulaEntra21_Thiago\\New Exercícios - Entra21 Python\\pessoas.txt", "a")
        file.write(f"{p1.id};{p1.nome};{p1.data_nasc};{p1.cpf};{p1.telefone};{p1.email};{p1.endereco}\n")
        file.close()

        file = open('C:\\Users\\thiago.zeferino\\Desktop\\Thiago Augusto Zeferino\\[Programas]\\AulaEntra21_Thiago\\New Exercícios - Entra21 Python\\dados_conta.txt', 'a')
        file.write(f'{p1.id};{cpf};{agencia};{p1.pergunta_secreta};{p1.resposta};{p1.senha};{p1.letras_secretas}\n')
        file.close()



class NuConta(Banco):
    def __init__(self ):
        super().__init__()

class Viacredi(Banco):
    def __init__(self):
        super().__init__()

class Conta():
    def __init__(self, banco:Banco, pessoa:Pessoa, numero:str, agencia:str, tipo_conta:int):
        self.banco = banco
        self.pessoa = pessoa
        self.numero = numero
        self.agencia = agencia
        self.tipo_conta = tipo_conta


print('\n                                 Começando...\n\n') # Alt
sleep(1) # Alt
Nu = NuConta() # Alt
Vi = Viacredi() #Alt
if __name__ == "__main__":
    while True:

        while True:
         # Alt
            try: # Coloquei Um Try aqui Para se O Usuario Escrever Errado, a Clausula Except irá consertar.
                valor = int(input(
                """\nDigite o Número Respectivo a Opcão Desejada: 

                1 - Cadastrar Conta
                2 - Visualizar Saldo
                3 - Fazer um depósito
                4 - Visualizar Dados
                5 - Sair\nR: """))
            except:
                print(10*'=', 'O Valor Foi Incorreto, Tente Novamente!', 10 * '=', '\n')
                sleep(2)
                # Except Irá receber o Erro, e Mostrar que foi incorreto, então irá retornar ao início.
            else: 
                break # Se o Erro não Ocorrer e o Usuário Escrever Corretamente, Então sairá desse Loop
       
############################################  Cadastramento Abaixo ################################################       

        if valor == 1:

        # Aqui irá Perguntar Qual Banco Ele Deseja Cadastrar.

            option_bank = input('''
Qual Banco Deseja Se Cadastrar?
  (Digite O Número Da Opção)

1 - Viacredi            2 - NuConta

R: ''')
            sleep(1)

            if option_bank == '1':
                print('Seu Cadastramento na Viacredi irá Começar...\n')
                Nu.cadastrar_pessoa()
                
            elif option_bank == '2':
                print('Seu Cadastramento na NuConta irá Começar...\n')
                Vi.cadastrar_pessoa()
                
            else:
                print(10 * '=', 'Você Digitou Incorretamente!', 10 * '=', '\n') # Se o Usuário Digitar algo diferente
            sleep(1)                                                            # De 1 ou de 2, cai no Else, e ao inicio.

################################################ Fim De Cadastramento ###################################################   

################################################ Visualizar Os Dados ###################################################

        if valor == 4:

            file = open('pessoas.txt', 'r') # Aqui Vai Ler o Arquivo
            for linha in file:
                linha_limpa = linha.strip()
                lista = linha_limpa.split(';')
                print('%')
                print(lista[0])
                print(*lista)
                print(lista)

                    
                identificacao = input('Qual É O Número Da Sua Conta?\nR: ')
        
                # Vai Verificar Se o Número da Conta Bate com o que foi Enviado ao txt
                if identificacao in lista:
                    print(lista[0])
                    pedir_senha = input('Qual É A Sua Senha de 7 Caractéres?\nR: ')
                    if pedir_senha == lista[9]:
                        pedir_letra_secreta = input('Quais São As Suas Letras Secretas?\nR: ').upper()
                        if pedir_letra_secreta == lista[10]:
                                    print(*lista)
                                    break
                    # Essa Parte Acima é Se Ele ACERTOU DE PRIMEIRA TUDO!     

                    # Se Errou a Letra Secreta e acertou a Senha
                        else:
                            while pedir_pergunta_secreta != lista[8]:
                                pedir_pergunta_secreta = ''
                                print(lista[7])
                                pedir_pergunta_secreta = input('R: ')
                            print(*lista)
                            break
                
                 
                                
                #Ignore Essa Parte ABAIXO Se Não For considerar que ele errou A Senha!

                    else:  # Vai Entrar Em Um loop Perguntando a pergunta Secreta se errou A SENHA !
                        print(10 * '=', 'INCORRETO!', 10 * '=', '\n') 
                        pedir_pergunta_secreta = ''
                        while pedir_pergunta_secreta != lista[8]:
                            print(lista[7])
                   ######## PERGUNTAR SE AQUI COLOCA UMA OPÇÃO DE SIM OU NÃO PARA CONTINUAR
                            pedir_pergunta_secreta = input('R: ')

                        # Por ter errado a senha, mas acertado a pergunta secreta, ele continua nesse outro caminho secundario
                        pedir_letra_secreta = input('Quais São As Suas Letras Secretas?\nR: ').upper()
                        if pedir_letra_secreta == lista[10]:
                            print(*lista)
                            break
                ####### Se Errou Novamente...(CONVERSAR SOBRE ESSA PARTE, POR ELE TER ERRADO 2 VEZES E JÁ TER USADO A PERGUNTA SECRETA, SERIA MELHOR SE O PROGRAMA ACABASSE AQUI)
                        else:
                            while pedir_pergunta_secreta != lista[8]:
                                pedir_pergunta_secreta = ''
                                print(lista[7])
                                pedir_pergunta_secreta = input('R: ')
                            # Se Errou Novamente, mas acertou a pergunta secreta (CONVERSAR SOBRE ESSA PARTE, POR ELE TER ERRADO 2 VEZES E JÁ TER USADO A PERGUNTA SECRETA, SERIA MELHOR SE O PROGRAMA ACABASSE AQUI)
                            print(*lista)
                            break

                # Se Lá No INÍCIO o NÚMERO DA CONTA Estava ERRADA!
                else:
                    print(10 * '=', 'ERRO! Não Foi Encontrado', 10 * '=', '\n')
            file.close()
                
        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
