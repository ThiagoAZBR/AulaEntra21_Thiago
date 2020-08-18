# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

a = int(input('Digite um número de 1 a 7 e veja o dia da semana: '))

if a == 7:
    print('Domingo')
if a == 6:
    print('Sábado')
if a == 5:
    print('Sexta')
if a == 4:
    print('Quinta-feira')
if a == 3:
    print('Quarta-feira')
if a == 2:
    print('Terça-Feira')
if a == 1:
    print('Segunda-Feira')
