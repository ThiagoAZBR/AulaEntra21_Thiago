# Exercicio 3
# Faça um programa que peça a idade do cliente.
# 
# Se ele tiver 18 anos ou mais deve aparecer a mensagem "Entrada permitida"
# 
# Caso contrário deve aparecer a mensagem "Entrada Negada!"

a = int(input('Qual a Sua Idade? \n R: '))

if a > 18 or a == 18:
    print('Entrada Permitida!!!')
else: 
    print('Entrada Negada!')