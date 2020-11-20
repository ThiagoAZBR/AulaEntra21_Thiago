import sqlite3

import sqlite3

DB_PATH = "clientes.db"


class Cliente:
    """Class to create client objects
    """
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email


class Veiculo:
    """Class to crete vehicle objects
    """
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color


class DataReader:
    """Class to Read data from a SQLite instance table
    """
    def __init__(self, db_path, table):
        self.db_path = db_path
        self.table = table
    
    def retrieve_all(self):
        """Retrieve all data within a given table
        """
        # Create connection with db and a cursor to handle data
        with sqlite3.connect(self.db_path) as conn:

            # Create a SQLite cursor
            c = conn.cursor()

            # Build SQL select command and execute it
            c.execute(f"SELECT * FROM {self.table}".replace("'", ""))
            
            # Fetch table data
            content = c.fetchall()
        
        # Return content as a list of tuples
        return content

class DataWriter:
    """Class to perform CRUD operations
    """
    # Constructor
    def __init__(self, obj):
        self.obj = obj
        self.table = type(obj).__name__.lower() + "s"
    
    def insert(self, db_path):
        """Method to insert data into SQLite instance
        """
        # Create connection with db and a cursor to handle data
        with sqlite3.connect(db_path) as conn:

            # Get instance attributes as a dictionary
            data = self.obj.__dict__

            # Create a SQLite cursor
            c = conn.cursor()
            
            # Build the SQL insert command
            query = "INSERT INTO {} {}".format(
                self.table, tuple(data.keys())
                )
            query += f" VALUES {('?',)*len(data)}"                      # Pedir Para Explicar Essa Parte!
            
            # Execute command and commit data
            c.execute(query.replace("'", ""), tuple(data.values()))    # O Erro Provavelmente Está Por Aquii!
            conn.commit()

    def update_info(self, db_path):
        pass

    def delete_data(self, db_path):
        pass

if __name__ == "__main__":

    # Criando a tabela de pessoas
    # conexion = sqlite3.connect('clientes.db')
    # cursor = conexion.cursor()

    # cursor.execute('''
    # ALTER TABLE clientes
    # ADD COLUMN email TEXT
    # ''')

    # cursor.execute("""
    # CREATE TABLE clientes (
    #         id_pessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #         nome TEXT NOT NULL,
    #         cpf TEXT NOT NULL);
    # """)

    # conexion.commit()
    # conexion.close()
    
    # Create Client instances
    c01 = Cliente("Peter", "189.892.312-99", "peter@yahoo.com")
    c02 = Cliente("John", "098.734.231-00", "john@amazon.com.uk")

    # Create Vechicle instances
    # v01 = Veiculos("Cadillac", "Navigator", "2014", "Silver")
    # v02 = Veiculos("Land Rover", "Discovery", "2016", "White")

    # Insert client data into clients table
    DataWriter(c01).insert(DB_PATH)
    DataWriter(c02).insert(DB_PATH)

    # Insert vehicle data into vechicles table
    # DataWriter(v01).insert(DB_PATH)
    # DataWriter(v02).insert(DB_PATH)

    # Fetch client and vehicle data and print it
    print(DataReader(DB_PATH, "clientes").retrieve_all())
    # print(DataReader(DB_PATH, "vehicles").retrieve_all())
