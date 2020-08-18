# Exercicio 10
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem decrescente.
# 

a = int(input('Qual o Primeiro número? '))
b = int(input('Qual o Segundo número?  '))
c = int(input('Qual o terceiro número?  '))

lista = [a, b, c]

print(f'A Ordem decrescente é {sorted(lista, reverse = True)}')
