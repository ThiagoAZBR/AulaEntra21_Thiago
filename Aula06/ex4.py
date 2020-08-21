a = int(input('Qual o valor do primeiro lado? '))
b = int(input('Qual o valor do segundo lado? '))
c = int(input('Qual o valor do terceiro lado? '))

if a >= b+c:
    print('Não Pode formar um triângulo.')
if b >= a+c:
    print('Não Pode formar um triângulo.')
if c >= a+b:
    print('Não Pode formar um triângulo.')
else:
    print('Pode formar um triângulo!')

if a == b == c :
    print('É um triângulo Equilátero!')
if a != b == c or b != c == a or c != a == b :
    print('É um triângulo Isósceles!')
if a != b != c:
    print('É um triangulo Escaleno!')
