import sys
import sqlite3
from classes import Cliente, Veiculo, DataReader, DataWriter
from time import sleep

DB_PATH = 'clientes.db'

# Funções clientes
def cadastro_clinte():
    pass

def alterar_cadastro_cliente():
    pass
def deletar_cliente():
    pass


# Funções veículos
def cadastro_veiculo():
    pass
def listar_veiculos():
    pass
def alterar_cadastro_veiculo():
    pass
def deletar_veiculo():
    pass


def menu_pessoas():
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
        
        if opcao == "1":
            cadastro_clinte()
        elif opcao == "2":
            print('========== ENTROU =========')
            
            clientes = DataReader(DB_PATH, "clientes").retrieve_all()
            def listar_clientes():

                if len(clientes) == 0:
                    print('Não Foi Encontrado!')
                else:
                    count = 0
                    quant = len(clientes)
                    print(f'''
=========================================================

                  - L I S T A G E M -

=========================================================

Existem {quant} Cliente(s) Cadastrado(s): ''')
                    sleep(2)
                    for linha in clientes:
                        count += 1
                        print(f'''
  - {count}°  C L I E N T E -

    I D      |  {linha[0]}
    N O M E  |  {linha[1]}
    C P F    |  {linha[2]} ''')
                        sleep(2)
                    opcao2 = input('\nDeseja Sair?\nR: ')
            listar_clientes()


        elif opcao == "3":
            alterar_cadastro_cliente()
        
        elif opcao == "4":
            deletar_cliente()
        
        elif opcao == "8":
            print("Retornando ao menu principal ...")
            break
        
        elif opcao == "9":
            sys.exit("\nSaindo, até logo! ... :(")
        
        else:
            print("Opção inválida!")
menu_pessoas()

def menu_veiculos():
    while True:
        print(" >> Dados dos veículos!")
        opcao = input("""
        [1] Cadastrar novo veículo
        [2] Listar veículos cadastrados
        [3] Alterar cadastro de veículo
        [4] Deletar cadastro de veículo
        [8] Voltar ao menu principal
        [9] Sair do sistema
        Digite uma opção: """)

        if opcao == "1":
            cadastro_veiculo()

        elif opcao == "2":
            listar_veiculos()

        elif opcao == "3":
            alterar_cadastro_veiculo()
        
        elif opcao == "4":
            deletar_veiculo()
        
        elif opcao == "8":
            print("Retornando ao menu principal ...")
            break
        
        elif opcao == "9":
            sys.exit("\nSaindo, até logo! ... :(")
        
        else:
            print("Opção inválida!")

def main():
    while True:
        print(" >> Bem vindo ao sistema CRUD 1.0!")
        opcao = input("""
        [1] Pessoas
        [2] Veículos
        [9] Sair do sistema
        Digite uma opção: """)

        if opcao == "1":
            menu_pessoas()

        elif opcao == "2":
            menu_veiculos()

        elif opcao == "9":
            sys.exit("\nSaindo, até logo! ... :(")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
