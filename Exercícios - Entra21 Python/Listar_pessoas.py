from Cadastrar_pessoas import cadastro
def retorna_pessoas():
    tam = len(cadastro['ide'])
    for i in range(tam):
        print(f'''
Nome: {cadastro['nome'][i]} {cadastro['sobrenome'][i]}
Idade: {cadastro['idade'][i]}''')
    
def retorna_pessoa_id(ide):
    print(f'''
Nome: {cadastro['nome'][ide]} {cadastro['sobrenome'][ide]}
Idade: {cadastro['idade'][ide]}''')
