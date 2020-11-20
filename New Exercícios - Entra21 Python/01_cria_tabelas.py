import sqlite3

# Cria conexão com banco de dados
conn = sqlite3.connect('crud_basico_clientes.db')

# Cria cursor para executar alterações no banco de dados
cursor = conn.cursor()

try:
    # Criando a tabela de veiculos
    # cursor.execute("""
    # CREATE TABLE carros (
    #         id_carro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT
    #         marca TEXT NOT NULL,
    #         modelo TEXT NOT NULL,
    #         ano VARCHAR(4) NOT NULL,
    #         cor TEXT NOT NULL,
    #         placa VARCHAR(8) NOT NULL,
    #         proprietario TEXT NOT NULL,
    #         num_portas INTEGER NOT NULL,
    #         km_rodado REAL NOT NULL,
    #         qtd_passageiros INTEGER NOT NULL,
    #         motor TEXT NOT NULL,
    #         combustivel TEXT NOT NULL,
    #         meio_locomocao TEXT NOT NULL,
    #         valor REAL NOT NULL
    # );
    # """)

    # Criando a tabela de pessoas
    cursor.execute("""
    CREATE TABLE pessoass (
            id_pessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,

    );
    """)

    # Indica criação da tabela
    print('Tabela criada com sucesso.')

    # Fechando a conexão
    conn.close()
except:
    print("Tabela já criada")