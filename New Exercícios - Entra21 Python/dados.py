# 12/11
def contar():
    file = open('conta.txt', 'r')
    quant = len(file.readlines())
    file.close()
    return quant

def visualizar_dados(identificacao, quant):
    cont = 0
    pedir_pergunta_secreta = ''
    file = open('conta.txt', 'r') # Aqui Vai Ler o Arquivo
    for linha in file:
        print('Entrou? ')
        cont += 1
        linha_limpa = linha.strip()
        lista = linha_limpa.split(';')
        print(lista[0])
        print(*lista)
        print(lista)

        # nome do Banco = 0
        # cpf = 1
        # agencia = 2
        # Número Da Conta = 3
        # senha = 4
        # pergunta = 5
        # resposta = 6
        # letra = 7    

        # Vai Verificar Se o Número da Conta Bate com o que foi Enviado ao txt
        if identificacao in lista:
            pedir_senha = input('Qual É A Sua Senha de 7 Caractéres?\nR: ')
            if pedir_senha == lista[5]:
                pedir_letra_secreta = input('Quais São As Suas Letras Secretas?\nR: ').upper()
                if pedir_letra_secreta == lista[6]:
                            print(*lista)
                            break
            # Essa Parte Acima é Se Ele ACERTOU DE PRIMEIRA TUDO!     

            # Se Errou a Letra Secreta e acertou a Senha
                else:
                    while pedir_pergunta_secreta != lista[6]:
                        pedir_pergunta_secreta = ''
                        print(lista[3])
                        pedir_pergunta_secreta = input('R: ')
                    print(*lista)
                    break
        
            
                        
        #Ignore Essa Parte ABAIXO Se Não For considerar que ele errou A Senha!

            else:  # Vai Entrar Em Um loop Perguntando a pergunta Secreta se errou A SENHA !
                print(10 * '=', 'INCORRETO!', 10 * '=', '\n') 
                pedir_pergunta_secreta = ''
                while pedir_pergunta_secreta != lista[2]:
                    print(lista[3])
################### PERGUNTAR SE AQUI COLOCA UMA OPÇÃO DE SIM OU NÃO PARA CONTINUAR
                    pedir_pergunta_secreta = input('R: ')

                # Por ter errado a senha, mas acertado a pergunta secreta, ele continua nesse outro caminho secundario
                pedir_letra_secreta = input('Quais São As Suas Letras Secretas?\nR: ').upper()
                if pedir_letra_secreta == lista[4]:
                    print(*lista)
                    break
        
                else:
                    print('Tente Novamente Mais Tarde!')

        # Se Lá No INÍCIO o NÚMERO DA CONTA Estava ERRADA!
        elif cont == quant:
            print(10 * '=', 'ERRO! Não Foi Encontrado', 10 * '=', '\n')
    file.close()