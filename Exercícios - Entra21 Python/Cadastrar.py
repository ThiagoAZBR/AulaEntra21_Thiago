cadastro = {}
nome_lista = []
sobrenome_lista = []
idade_lista = []
ide_lista = []
def cadastrar(nome, sobrenome, idade, ide):

    if idade >= 18:
        nome_lista.append(nome)
        cadastro['nome'] = nome_lista
        sobrenome_lista.append(sobrenome)
        cadastro['sobrenome'] = sobrenome_lista
        idade_lista.append(idade)
        cadastro['idade'] = idade_lista
        ide_lista.append(ide)
        cadastro['ide'] = ide_lista
        return ide
    else:
        print('\nIdade inválida!')
        return ide * -1
