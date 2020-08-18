# Exercicio 18
# Peça para o usuário digitar os valores de a, b e c
# 
# Calcule o delta "delta = (b**2)-(4*a*c)"
# 
# Se o delta der negativo, então deve aparecer a seguinte mensagem: "Delta negativo! Equação não pode ser resolvida!"
# 
# Se o delta der igual a zero, então deve aparecer a seguinte mensagem: "Delta igual a zero!"
# 
# Se o delta der positivo, então deve aparecer a seguinte mensagem: "A equação pode ser resolvida!"

a = int(input('Qual o Valor de a? \n R: '))

b = int(input('Qual o Valor de b? \n R: '))

c = int(input('Qual o Valor de c? \n R: '))

delta = b**2 -4*a*c

print(f'O Valor de Delta é {delta}')

if delta < 0:
    print('Delta Negativo! Equação Não pode ser resolvida!')
if delta > 0:
    print('A equação pode ser resolvida!')
if delta == 0:
    print('O Delta é 0!')

