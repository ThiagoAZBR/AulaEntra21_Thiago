# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 
litro = float(input('Quantos litros deseja abastecer? '))
tipo = int(input('Qual tipo de combustivel deseja? Digite o respectivo número: \n \n 1 - álcool \n 2 - diesel \n 3 - gasolina \n \n R: '))

if tipo == 1 and litro > 10:
    print(f'Você que {litro} litros, e {tipo} Seu desconto foi de 10%')
if tipo == 2 and litro > 10 :
     print(f'Você que {litro} litros, e {tipo} Seu desconto foi de 5%')
if tipo == 3 and litro > 20:
     print(f'Você que {litro} litros, e {tipo} Seu desconto foi de 10%')

if tipo == 1 and litro <10 :
     print(f'Você que {litro} litros, e {tipo} Seu desconto foi de 5%')
if tipo == 2 and litro < 10 :
     print(f'Você que {litro} litros, e {tipo} Seu desconto foi de 1,5%')
if tipo == 3 and litro < 20:
     print(f'Você que {litro} litros, e {tipo} Seu desconto foi de 0%')