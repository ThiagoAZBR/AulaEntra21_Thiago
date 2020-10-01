a, b, c = input().split()

pi = 3.14159

formula_rectangle_triangle_area = float(a) * float(c) / 2.0
formula_circle_area = pi * float(c) ** 2.0
formula_trapeze_area = (float(a) + float(b)) * float(c) / 2.0
formula_square_area = float(b) ** 2.0
formula_rectangle_area = float(a) * float(b)

print(f'TRIANGULO: {formula_rectangle_triangle_area:.3f}')
print(f'CIRCULO: {formula_circle_area:.3f}')
print(f'TRAPEZIO: {formula_trapeze_area:.3f}')
print(f'QUADRADO: {formula_square_area:.3f}')
print(f'RETANGULO: {formula_rectangle_area:.3f}')