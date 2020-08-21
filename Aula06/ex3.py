option = input('Digite A Letra correspondente a opção que Deseja: \n \n A) Soma \n B) Média \n C) Divisão \n D) Sair \n \n R: ')


if option.upper() == 'A' :
    a = int(input('Qual o primeiro número? '))
    b = int(input('Qual o segundo número? '))
    print(f'A soma de {a} e {b} é {a + b}')

if option.upper() == 'B':
    a = float(input('Qual a Primeira Nota do Aluno? \n R: '))
    b = float(input('Qual a Segunda Nota do Aluno? \n R: '))
    c = float(input('Qual a Terceira Nota do Aluno? \n R: '))
    d = float(input('Qual a Quarta Nota do Aluno? \n R: '))
    print(f'A média é {(a + b + c + d) / 2}')
if option.upper() == 'C':
    a = float(input('Qual o primeiro número? \n R: '))
    b = float(input('Qual o segundo número? \n R: '))
    if b == 0:
        print('Não se pode dividir por 0')
    if b != 0:
        print(f'A Divisão de {a} por {b} é {a / b}')
if option.upper() == 'D':
    print('Muito Obrigado E Volte Sempre!')