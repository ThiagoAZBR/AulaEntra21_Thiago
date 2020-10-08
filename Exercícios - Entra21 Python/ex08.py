#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função
'''                                         Aula de Funções                                                         '''
from time import sleep

print('Cálculo de Raizes...')
sleep(1)

def root():
    index = int(input('Digite O índice: '))
    rooting = int(input('Digite O Radicando: '))
    calculation = rooting ** (1/index)
    sleep(1)
    print('O Resultado é ', end = '')
    return calculation

print(f'{root():.2f}')