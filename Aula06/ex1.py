#Execicios 01

#Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

#Venda Total
#de R$ 0.00 a R$ 30000.00 - 0%
#de R$ 30000.01 a R$ 50000.00 - 1.5%
#de R$ 50000.01 a R$ 100000.00 - 2.5%
#Acima de R$ 100000.00 - 3.5%

total = float(input('Qual O Valor Total de venda? '))


if total > 0 and total <= 30000.00 :
    print(f'A Porcentagem de Comissão é 0%')

if total > 30000.00 and total <= 50000.00 :
    print(f'A Porcentagem de Comissão é 1.5%, dando o valor R$: {(total * 1.5) / 100}')

if total > 50000.00 and total <= 100000.00 :
    print(f'A Porcentagem de Comissão é 2.5%, dando o valor R$: {(total * 2.5) / 100}')

if total > 100000.00 :
    print(f'A Porcentagem de Comissão é 3.5%, dando o valor R$: {(total * 3.5) / 100}')
