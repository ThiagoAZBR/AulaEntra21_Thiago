# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

prod1 = input('Qual o Nome do primeiro produto? ')
prod2 = input('Qual o Nome do segundo produto? ')

quant1 = int(input(f'Quantas(os) de {prod1} você comprou? '))
quant2 = int(input(f'Quantas(os) de {prod2} você comprou? '))

val1 = float(input(f'E Quanto custa a ou o {prod1}? '))
val2 = float(input(f'E Quanto custa a ou o {prod2}? '))

print(f'Você comprou {quant1} {prod1}, cada um(a) custa {val1:.2f}. O Total foi R$: {quant1 * val1:.2f}')
print(f'Você também comprou {quant2} {prod2}, cada um(a) custa {val2:.2f}. O Total foi R$: {quant2 * val2:.2f}')

