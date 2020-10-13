from Cadastrar import cadastro
rua_lista = []
numero_lista = []
complemento_lista = []
bairro_lista = []
cidade_lista = []
estado_lista = []

def cad_end(ide, rua, numero, complemento, bairro, cidade, estado):
    if rua == '' or numero == '' or complemento == '' or bairro == '' or cidade == '' or estado =='':
        print("\nCadastro inválido! Campo vazio!")
    else:
        rua_lista.append(rua)
        cadastro['rua'] = rua_lista
        numero_lista.append(numero)
        cadastro['numero'] = numero_lista
        complemento_lista.append(complemento)
        cadastro['complemento'] = complemento_lista
        bairro_lista.append(bairro)
        cadastro['bairro'] = bairro_lista
        cidade_lista.append(cidade)
        cadastro['cidade'] = cidade_lista
        estado_lista.append(estado)
        cadastro['estado'] = estado_lista
        print("\nCadastro realizado com sucesso!")
    
    