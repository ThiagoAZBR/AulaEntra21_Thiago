a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

if (b ** 2) - (4 * a * c) <= 0:
    print('Impossivel calcular')
else:
    calculation_one = ( -b + ( ( b ** 2 - 4 * a * c ) ** (1/2)) ) / (2 * a)
    calculation_two = (- b - ( ( b ** 2 - 4 * a * c ) ** (1/2)) ) / (2 * a)
    print(f'R1 = {calculation_one:.5f}')
    print(f'R2 = {calculation_two:.5f}')