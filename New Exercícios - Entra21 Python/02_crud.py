import sqlite3
from time import sleep

# Standard library import
import sys

# Importando classes e metodos
from classes import Cliente, Veiculo, DataReader, DataWriter 

# Indica caminho para arquivo com base de dados
DB_PATH = "clientes.db"


def menu_clientes():
    """Menu para trabalhar com dados dos clientes
    """
    # Apresenta opções para menu de clientes
    while True:
        print("\n >> Dados do cliente!")
        opcao = input("""
        [1] Cadastrar novo cliente
        [2] Listar clientes cadastrados
        [3] Alterar cadastro de cliente
        [4] Deletar cadastro de cliente
        [8] Voltar ao menu principal
        [9] Sair do sistema
        Digite uma opção: """)

        # Realizar novo cadastro
        if opcao == "1":
            c = Cliente(
                input("Digite nome cliente: "),
                input("Digite o cpf: "), 
                input("Digite o email: ")
            )

            # Inserção do cliente no banco
            DataWriter(DB_PATH, "clientes").insert(c)

        # Apresentar clientes em tela
        elif opcao == "2":

            # Recupera informações de cliente    
            clientes = DataReader(DB_PATH, "clientes").retrieve_all()
            
            # Apresenta cabeçalho
            def listar_clientes():

                if len(clientes) == 0:
                    print('\nNão Foi Encontrado!\n')
                else:
                    
                    quant = len(clientes)
                    print(f'''
=========================================================

                  - L I S T A G E M -

=========================================================

Existem {quant} Cliente(s) Cadastrado(s)! ''')
                    

################### MODIFICANDO AQUI    20/11/2020 #####################################################
                    
                    print('\n\nEscolha Uma Opção De Visualização:')
                    conectar = sqlite3.connect('clientes.db')

                    cursor = conectar.cursor()

                    while True:

                        opcao_visualizar = input(''' 
    1 - Filtrar Por Nome
    2 - Filtrar Por Naturalidade
    3 - Filtrar Por CPF
    4 - Ver Todos
    5 - Sair Da Visualização

    Digite o Número Respectivo a Ação Que Deseja:\n   R:  ''')

###################### - Nome - ######################################################################
                        
                        if opcao_visualizar == '1':
                            count = 0
                            qual_nome = input('\nDigite Um Nome ou letra(s): ').capitalize()
                            cursor.execute(f'''
SELECT * FROM clientes
WHERE nome LIKE '{qual_nome}%';
''')                    
                            dados = cursor.fetchall()

                            if len(dados) == 0:
                                print(f'\nNão Foi Encontrado Nenhume {qual_nome}!')
                            else:
                                print('\n=========================================================')
                                for linha in dados:
                                    count += 1
                                    print(f'''
        - {count}°  C L I E N T E -

    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')

                            print('\n=========================================================')

                            qualquer = input('Aperte Enter Para Continuar: ')

######################## - CIDADE - ####################################################################

                        elif opcao_visualizar == '2':
                            count = 0
                            qual_cidade = input('\nDigite Uma Cidade: ')
                            cursor.execute(f'''
SELECT * FROM clientes
WHERE naturalidade LIKE '%{qual_cidade}%';
''')                    
                            dados = cursor.fetchall()

                            if len(dados) == 0:
                                print(f'\nNão Foi Encontrado Nenhuma Cidade com nome de {qual_cidade}!')
                            else:
                                print('\n=========================================================')
                                for linha in dados:
                                    count += 1
                                    print(f'''
        - {count}°  C L I E N T E -

    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')
                            print('\n=========================================================')
                            qualquer = input('Aperte Enter Para Continuar: ')
                        
############################## - CPF - ##################################################
                        elif opcao_visualizar == '3':
                            count = 0
                            qual_cpf = input('\nDigite Um CPF: ')
                            cursor.execute(f'''
SELECT * FROM clientes
WHERE cpf LIKE '%{qual_cpf}%';
''')                    
                            dados = cursor.fetchall()

                            if len(dados) == 0:
                                print(f'\nNão Foi Encontrado Nenhum CPF Com Esses Números: {qual_cpf}!')
                            else:
                                print('\n=========================================================')
                                for linha in dados:
                                    count += 1
                                    print(f'''
        - {count}°  C L I E N T E -

    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')
                            print('\n=========================================================')
                            qualquer = input('Aperte Enter Para Continuar: ')


######################### - Mostrar Tudo - ##########################################
                        elif opcao_visualizar == '4':
                            count = 0
            # Apresenta Os Dados Da Função
                            for linha in clientes:
                                count += 1
                                print(f'''
        - {count}°  C L I E N T E -

    I D                        |  {linha[0]}
    N O M E                    |  {linha[1]}
    N A S C I M E N T O        |  {linha[2]}
    C P F                      |  {linha[3]}
    E N D E R E Ç O            |  {linha[4]}
    S A L Á R I O              |  {linha[5]}
    P R O F I S S Ã O          |  {linha[6]}
    E M A I L                  |  {linha[7]}
    T E L E F O N E            |  {linha[8]}
    R E S P O N S A V E L      |  {linha[9]}
    S E X O                    |  {linha[10]}
    N A T U R A L I D A D E    |  {linha[11]}
    N A C I O N A L I D A D E  |  {linha[12]}
''')
                            qualquer = input('Aperte Enter Para Continuar: ')

######################### - Sair - ###########################################
                        elif opcao_visualizar == '5':
                            print('\nSaindo...')
                            break
                        
                        else:
                            print('\n', '=' * 15, 'Incorreto!', '=' * 15)


##################### - Termina Aqui A Modificação - #########################################################


            listar_clientes()

            # Apresenta rodapé
            print("\n" + "*"*60)    
                
        # Altera cadastro de cliente
        elif opcao == "3":
            alterar_cadastro_cliente()
            pass
        
        # Deleta registro de cliente
        elif opcao == "4":
            deletar_cliente()
            pass
        
        # Retorna ao menu principal
        elif opcao == "8":
            print("\n        Retornando ao menu principal ...")
            break
        
        # Sai do sistema
        elif opcao == "9":
            sys.exit("\n        Saindo, até logo! ...\n")
        
        # Indica opção inválida
        else:
            print("        Opção inválida!")


def menu_veiculos():
    """Menu Veiculos
    """
    while True:
        print("\n >> Dados dos veículos!")
        opcao = input("""
        [1] Cadastrar novo veículo
        [2] Listar veículos cadastrados
        [3] Alterar cadastro de veículo
        [4] Deletar cadastro de veículo
        [8] Voltar ao menu principal
        [9] Sair do sistema
        Digite uma opção: """)

        # Realizar novo cadastro
        if opcao == "1":
            pass
        
        # Apresentar veiculos em tela
        elif opcao == "2":
            pass
        
        # Altera cadastro de veiculo
        elif opcao == "3":
            pass
        
        # Deleta veiculo cadastro
        elif opcao == "4":
            pass
        
        # Retorna ao menu principal
        elif opcao == "8":
            print("\n        Retornando ao menu principal ...")
            break
        
        # Sai do sistema
        elif opcao == "9":
            sys.exit("\n        Saindo, até logo! ...\n")
        
        # Indica opção inválida
        else:
            print("        Opção inválida!")


def main_menu():
    """Menu Principal
    """
    while True:
        print("\n >> Bem vindo ao sistema CRUD 1.0!")
        opcao = input("""
        Deseja manipular quais registros?
        [1] Pessoas
        [2] Veículos
        [9] Sair do sistema
        Digite uma opção: """)

        # Opção para trabalhar com tabela de clientes
        if opcao == "1":
            menu_clientes()

        # Opção para trabalhar com tabela de veiculos
        elif opcao == "2":
            menu_veiculos()

        # Opção para sair do sistema
        elif opcao == "9":
            print("\n        Saindo, até logo! ... \n")
            break
        
        # Indica opção inválida
        else:
            print("        Opção inválida!")


if __name__ == "__main__":
    # Inicializa sistema
    main_menu()