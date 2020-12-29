
# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 50, 2% de desconto
# se o valor for superior a 100, 5% de desconto
# se o valor for superior a 200, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética

from time import sleep
from random import randint

print('\n                                                                     C O M E Ç A N D O...')

sleep(1)

lista_itens = ['Arroz', 'Feijão', 'Macarrão', 'Sal', 'Panela', 'Colher de pau', 'Fogão']

lista_valores = []

for a in range(0, len(lista_itens)):
    A = randint(0, 500)
    lista_valores.append(A)
'''
lista_valores = [250, 18, 16, 6.50, 89, 8.90, 500]
'''
numero = len(lista_valores)

string = ' \n'.join(lista_itens)

original = sum(lista_valores)

print(f'''
Sua Lista De Compras É:
{string} \n''')

sleep(3)
total = []
for a in range(0, numero):
    
    sleep(4)
    if lista_valores[a] > 50 and lista_valores[a] <= 100:
        valor = lista_valores[a]
        calculo = valor * 2 / 100
        calculo = lista_valores[a] - calculo
        total.append(calculo)
        print(f'O Desconto sobre o valor do {lista_itens[a]} vai ser de 2%, Você irá pagar R$: {calculo:.2f}, O Preço Original da(o) {lista_itens[a]} era R$: {valor}\n')
    
    elif lista_valores[a] > 100 and lista_valores[a] <= 200:
        valor = lista_valores[a]
        calculo = valor * 5 / 100
        calculo = lista_valores[a] - calculo
        total.append(calculo)
        print(f'O Desconto sobre o valor do {lista_itens[a]} vai ser de 5%, Você irá pagar R$: {calculo:.2f}, O Preço Original da(o) {lista_itens[a]} era R$: {valor}\n')

    elif lista_valores[a] > 200:
        valor = lista_valores[a]
        calculo = valor * 10 / 100
        calculo = valor - calculo
        total.append(calculo)
        print(f'O Desconto sobre o valor do {lista_itens[a]} vai ser de 10%, Você irá pagar R$: {calculo:.2f}, O Preço Original da(o) {lista_itens[a]} era R$: {valor}\n')
    
    else:
        valor = lista_valores[a]
        total.append(valor)
        print(f'A(O) {lista_itens[a]} não irá receber desconto por não atingir o preço mínimo, você irá pagar o preço Original da(o) {lista_itens[a]} que é R$: {lista_valores[a]}\n')
    sleep(4)


carero = max(lista_valores)
local = lista_valores.index(carero)

soma = sum(total)

sleep(2)

print(f'''
O Produto Mais Caro da Lista:
{string}
Seria o {lista_itens[local]} Com o Valor de R$: {carero} \n''')

sleep(1)

print(f'O Total de Gastos da Compra foi: R$: {soma} \n Sem os Descontos Ficaria R$: {original} \n')
