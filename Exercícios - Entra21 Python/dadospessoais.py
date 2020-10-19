'''                     Função  Para  Mandar  Para  O  Arquivo                                      '''


from Cadastrar_pessoas import nome_lista
from Cadastrar_pessoas import sobrenome_lista
from Cadastrar_pessoas import idade_lista


def gerar_id():
    arquivo = open('DadosPessoas.txt', 'r')
    numero_l = len(arquivo.readlines())
    return numero_l + 1

number = gerar_id()

def adicionar_texto_pessoas():
    arquivo = open('DadosPessoas.txt', 'a')
    arquivo.write(f'{nome_lista[0]};{sobrenome_lista[0]};{idade_lista[0]};{number}\n')
    arquivo.close()

def ler_texto_pessoas(ide):
    arquivo = open('DadosPessoas.txt', 'r')
    for linha in arquivo:
        linha_limpa = linha.strip()   
        lista_dados = linha_limpa.split(';')
        ide = str(ide)
    if ide in lista_dados :
        print(f'''
        Nome: {lista_dados[0]}
        Sobrenome {lista_dados[1]}
        Idade: {lista_dados[2]}  
          ''')
    else:
        print(20 * '-=' + '-', 'Não Foi Encontrado', 20 * '-=' + '-')
