def gerar_id():
    arquivo = open('Pessoa.txt', 'r')
    numero_l = len(arquivo.readlines())
    return numero_l + 1

def adicionar_texto_pessoas(nome, sobrenome, idade):
    number = gerar_id()
    arquivo = open('Pessoa.txt', 'a')
    arquivo.write(f'{nome};{sobrenome};{idade};{number}\n')
    arquivo.close()
    return number

def ler_texto_pessoas(ide):
    arquivo = open('Pessoa.txt', 'r')
    for linha in arquivo:
        linha_limpa = linha.strip()   
        lista_dados = linha_limpa.split(';')
        ide = str(ide)
        if ide in lista_dados :
            print(f'\nNome: {lista_dados[0]}\nSobrenome: {lista_dados[1]}\nIdade: {lista_dados[2]}')
