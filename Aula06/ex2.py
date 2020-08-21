#Escreva um programa que receba 4 notas e calcule a média.
#Mostre a seguinte mensagem conforme a media final.
#Media Final
#de 0 a 5 - Reprovado
#de 5 a 6.5 - Recuperação
#de 6.5 a 9 - Aprovado
#Acima de 9 - Aprovado com louvor

a = float(input('Qual a Primeira Nota do Aluno? \n R: '))
b = float(input('Qual a Segunda Nota do Aluno? \n R: '))
c = float(input('Qual a Terceira Nota do Aluno? \n R: '))
d = float(input('Qual a Quarta Nota do Aluno? \n R: '))

media = (a + b + c + d) /4

if media >= 0 and media <= 5 :
    print(f'A Média foi {media}, o aluno foi REPROVADO!')

if media > 5 and media <= 6.5 :
    print(f'A Média foi {media}, o aluno está em RECUPERAÇÂO!')

if media > 6.5 and media <= 9 :
    print(f'A Média foi {media}, o aluno foi APROVADO!')
    
if media > 9 :
    print(f'A Média foi{media}, o Aluno foi APROVADO COM EXCELÊNCIA!')
