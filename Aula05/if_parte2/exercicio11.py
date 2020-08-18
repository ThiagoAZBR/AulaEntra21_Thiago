
# Exercicio 11
# Faça um programa que peça o sexo do cliente. 
# 
# Se o cliente digitar 'F' deve aparecer a mensagem "Como você está bonita hoje!"
# 
# Se o cliente digitar 'M' deve aparecer a mensagem "Como você está forte? andou malhando?"
# 
# Se o cliente digitar qualquer outra coisa, deve aparecer a mensagem: "opção invalida!"
# 

a = input('Qual Seria o seu Gênero? ')

if a == 'M':
    print('Você está lindo hoje. Você faz Academia?')
if a == 'F':
    print('Você está Maravilhosa. Como foi seu dia?')
if a != 'F' and a != 'M':
    print('Não Importa seu gênero, você é Incrivel!')