#--- Exercício 4  - Funções
#--- Crie uma função que imprima um cabeçalho de acordo com uma variável de nome da empresa (passada por parametro)
#--- A impressão deve ocorrer via multiplicação de strings
#--- A multiplicação deve ser feita com base em uma variável que contenha o caracter a ser multiplicado
#--- Crie uma segunda função que imprima um rodapé utilizando a mesma técnica
#--- Crie uma chamada para as duas função, para exibir o resultado no console
'''                                         Aula de Funções                                                         '''
def header(espelho):
    keep_it_beatiful = 20 * '-=' + '-'
    print(keep_it_beatiful, espelho, keep_it_beatiful)

def footer(espelho2):
    stay_beatiful = 20 * '-=' + '-'
    print(stay_beatiful, espelho2, stay_beatiful)

a = input('Digite o Nome da Empresa Para o Cabeçalho: ')
b = input('Digite Novamente o Nome da Empresa para o Rodapé: ')

header(a)
footer(b)
