lista = []

from time import sleep

for a in range(0,3):
    nota = float(input('Digite A Nota: '))
    lista.append(nota)
    
media = sum(lista) / len(lista)

sleep(0.5)
print('\nCalculando...')

sleep(1)

print(f'\nA média do aluno foi {media:.2f}\n')
