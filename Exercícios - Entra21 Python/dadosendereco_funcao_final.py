def adicionar_texto_endereco(rua, numero, complemento, bairro, cidade, estado, ide):
    arquivo = open('Endereco.txt', 'a')
    arquivo.write(f'{rua};{numero};{complemento};{bairro};{cidade};{estado};{ide}\n')
    arquivo.close()

def ler_texto_endereco(ide):
    arquivo = open('Endereco.txt', 'r')
    for linha in arquivo:
        linha_limpa = linha.strip()   
        lista_dados = linha_limpa.split(';')
        ide = str(ide)

        if ide in lista_dados :
            print(f'''Rua: {lista_dados[0]}
Número de Residência: {lista_dados[1]}
Complemento: {lista_dados[2]}
Bairro: {lista_dados[3]}
Cidade: {lista_dados[4]}
Estado: {lista_dados[5]}
        ''')

def ler_todos_dados():
    arquivo = open('Pessoa.txt', 'r')
    tam = len(arquivo.readlines())
    for i in range(tam+1):
        arquivo = open('Pessoa.txt', 'r')
        for linha in arquivo:
            linha_limpa = linha.strip()   
            lista_dados = linha_limpa.split(';')
            ide = str(i+1)
            if ide in lista_dados :
                print(f'\nNome: {lista_dados[0]}\nSobrenome: {lista_dados[1]}\nIdade: {lista_dados[2]}')
    
        arquivo = open('Endereco.txt', 'r')
        for linha in arquivo:
            linha_limpa = linha.strip()   
            lista_dados = linha_limpa.split(';')
            ide = str(ide)
            if ide in lista_dados :
                print(f'''Rua: {lista_dados[0]}
Número de Residência: {lista_dados[1]}
Complemento: {lista_dados[2]}
Bairro: {lista_dados[3]}
Cidade: {lista_dados[4]}
Estado: {lista_dados[5]}
        ''')
