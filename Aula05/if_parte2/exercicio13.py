# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua Idade? ')
endereço = input('Qual é o seu endereço? ')
email = input('Qual é o seu email? ')
telefone = input('Qual é o seu telefone? ')

option = input('Escreve Qual Você deseja selecionar: \n \n Dados \n Endereço \n Contato \n \n R: ')

if option == 'Dados' or option == 'dados' :
    print(f'O seu nome: {nome} \n Idade: {idade}')

if option == 'Endereço' or option == 'endereço' :
    print(f'O seu nome: {nome} \n Endereço: {endereço}')

if option == 'Contato' or option == 'contato' :
    print(f'O seu nome: {nome}\n Email: {email} \n Telefone: {telefone}')





