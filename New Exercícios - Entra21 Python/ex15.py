# 12/11
file = open('dados_conta.txt', 'w')
file.write('Aqui')
file.close()

def visualizar_dados():

    file = open('C:\\Users\\thiago.zeferino\\Desktop\\Thiago Augusto Zeferino\\[Programas]\\AulaEntra21_Thiago\\New Exercícios - Entra21 Python\\dados_conta.txt', 'r') # Aqui Vai Ler o Arquivo
    for linha in file:
        linha_limpa = linha.strip()
        lista = linha_limpa.split(';')
        print('%')
        print(lista[0])
        print(*lista)
        print(lista)

        # num conta = 0
        # cpf = 1
        # agencia = 2
        # pergunta = 3
        # resposta = 4
        # senha = 5
        # letra = 6    
        identificacao = input('Qual É O Número Da Sua Conta?\nR: ')

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
                    while pedir_pergunta_secreta != lista[4]:
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
            ######## PERGUNTAR SE AQUI COLOCA UMA OPÇÃO DE SIM OU NÃO PARA CONTINUAR
                    pedir_pergunta_secreta = input('R: ')

                # Por ter errado a senha, mas acertado a pergunta secreta, ele continua nesse outro caminho secundario
                pedir_letra_secreta = input('Quais São As Suas Letras Secretas?\nR: ').upper()
                if pedir_letra_secreta == lista[4]:
                    print(*lista)
                    break
        ####### Se Errou Novamente...(CONVERSAR SOBRE ESSA PARTE, POR ELE TER ERRADO 2 VEZES E JÁ TER USADO A PERGUNTA SECRETA, SERIA MELHOR SE O PROGRAMA ACABASSE AQUI)
                else:
                    while pedir_pergunta_secreta != lista[4]:
                        pedir_pergunta_secreta = ''
                        print(lista[3])
                        pedir_pergunta_secreta = input('R: ')
                    # Se Errou Novamente, mas acertou a pergunta secreta (CONVERSAR SOBRE ESSA PARTE, POR ELE TER ERRADO 2 VEZES E JÁ TER USADO A PERGUNTA SECRETA, SERIA MELHOR SE O PROGRAMA ACABASSE AQUI)
                    print(*lista)
                    break

        # Se Lá No INÍCIO o NÚMERO DA CONTA Estava ERRADA!
        else:
            print(10 * '=', 'ERRO! Não Foi Encontrado', 10 * '=', '\n')
    file.close()