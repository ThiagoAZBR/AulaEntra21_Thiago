# Exercicio 4
# Escreva um programa que peça a nota de um aluno
# 
# Se a nota for 7 ou mais deve aparecer a mensagem: "Aprovado"
# 
# Caso contrário deve aparecer a mensagem: "Reprovado"

nota = float(input('Qual a Nota? \n R: '))

if nota > 7 or nota == 7:
    print('Aprovado!')
else:
    print('Reprovado!')
    