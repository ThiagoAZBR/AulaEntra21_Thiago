
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.


cliente = input('Qual O Seu Nome? ')

quant = int(input('Quantos Vai levar? '))

preço = float(input('Quanto custa?'))

print(f'Olá {cliente}, o total foi R$:{quant * preço}')
