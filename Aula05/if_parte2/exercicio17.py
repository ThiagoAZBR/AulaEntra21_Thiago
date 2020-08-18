# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"

a = int(input('Qual a Primeiro nota? '))
b = int(input('Qual a Segundo nota?  '))
c = int(input('Qual a terceiro nota?  '))
d = int(input('Qual a quarta nota?  '))

media = (a + b + c + d) /4

if media == 7 or media > 7:
    print('Aprovado!')
if media < 7 :
    print('Reprovado!')
if media == 10 :
    print('Aprovado Com Louvor! \n')
print(media)