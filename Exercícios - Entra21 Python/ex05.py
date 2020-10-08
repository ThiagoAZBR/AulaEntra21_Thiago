#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string
'''                                         Aula de Funções                                                         '''
def divided_calculation():
    a = float(input('First Number: '))
    b = float(input('Second Number: '))
    divided_value = a / 2
    print('\nO Resultado é: ', end = '')
    return divided_value

print(divided_calculation())
