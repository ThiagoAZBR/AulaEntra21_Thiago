'''                     Função  Para  Mandar  Para  O  Arquivo                                      '''

from function_ex10 import lista_rua
from function_ex10 import lista_numero
from function_ex10 import lista_complemento
from function_ex10 import lista_bairro
from function_ex10 import lista_cidade
from function_ex10 import lista_estado

def gerar_id():
    arquivo = open('DadosEndereco.txt', 'r')
    numero_l = len(arquivo.readlines())
    return numero_l + 1

number = gerar_id()

def adicionar_texto_endereco():
    arquivo = open('DadosEndereco.txt', 'a')
    arquivo.write(f'{lista_rua[0]};{lista_numero[0]};{lista_complemento[0]};{lista_bairro[0]};{lista_cidade[0]};{lista_estado[0]};{number}\n')
    arquivo.close()

def ler_texto_endereco(ide):
    arquivo = open('DadosEndereco.txt', 'r')
    for linha in arquivo:
        linha_limpa = linha.strip()   
        lista_dados = linha_limpa.split(';')
        ide = str(ide)
    if ide in lista_dados :
        print(f'''
        Rua: {lista_dados[0]}
        Número de Residência: {lista_dados[1]}
        Complemento: {lista_dados[2]}
        Bairro: {lista_dados[3]}
        Cidade: {lista_dados[4]}
        Estado: {lista_dados[5]}
        ''')
    else:
        print(20 * '-=' + '-', 'Não Foi Encontrado', 20 * '-=' + '-')