from Cadastrar import cadastro

def retorna_enderecos():
    tam = len(cadastro['ide'])
    for i in range(tam):
        print(f'''Rua: {cadastro['rua'][i]}
Numero: {cadastro['numero'][i]}
Complemento: {cadastro['complemento'][i]}
Bairro: {cadastro['bairro'][i]}
Cidade: {cadastro['cidade'][i]} 
Estado: {cadastro['estado'][i]}
        ''')

def retorna_end_id(ide):
    print(f'''Rua: {cadastro['rua'][ide]}
Numero: {cadastro['numero'][ide]}
Complemento: {cadastro['complemento'][ide]}
Bairro: {cadastro['bairro'][ide]}
Cidade: {cadastro['cidade'][ide]} 
Estado: {cadastro['estado'][ide]}
        ''')