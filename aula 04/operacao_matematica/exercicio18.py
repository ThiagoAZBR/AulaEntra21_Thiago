# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.

a = int(input('Qual o Valor de a? \n R: '))

b = int(input('Qual o Valor de b? \n R: '))

c = int(input('Qual o Valor de c? \n R: '))

delta = b**2 -4*a*c

print(f'O Valor de Delta é {delta}')
