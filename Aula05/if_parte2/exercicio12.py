# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.


a = int(input('Qual o Primeiro número? '))
b = int(input('Qual o Segundo número?  '))

option = int(input(' Escolha uma das 5 opções para calcular, digitando seu respectivo número: \n \n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Exponenciação \n \n R: '))

if option == 1 :
    print(f'O Resultado é {a + b}!')

if option == 2 :
    print(f'O Resultado é {a - b}!')

if option == 3 :
    print(f'O Resultado é {a * b}!')

if option == 4 :
    print(f'O Resultado é {a / b}!')

if option == 5 :
    print(f'O Resultado é {a ** b}!')

