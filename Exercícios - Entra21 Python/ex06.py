#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
'''                                         Aula de Funções                                                         '''
def avarage_calculation():
    a = float(input('First Number: '))
    b = float(input('Second Number: '))
    c = float(input('Third Number: '))
    grade = [] # Cria a Lista Para Armazenar as Notas.
    grade.append(a)
    grade.append(b)
    grade.append(c) # Aqui já está tudo Armazenado.
    average_value = (sum(grade)) / len(grade) # Aqui Descobrimos a Média somando os itens da lista, depois dividindo pela quantidade de itens na lista.
    print('A Média Do Aluno Foi de ', end = '')
    return average_value

print(avarage_calculation())

