nome = input('Nome: ') 
idade = input('Idade: ')
animal = input('Tem Animais? \n R: ')

animal = animal.lower()
if animal == 'não' or animal == 'n':
    print('')
else :
    quant = input('Quantos Animais Você tem? \n R: ')
    what = input('Que tipo de Animais são? \n R: ')


arquivo = open('Arquivo.txt', 'w')
arquivo.write(f'{nome}\n{idade}\n{animal}\n')
if animal == 'sim' or animal == 's':
    arquivo.write(f'{quant}\n{what}\n')
arquivo.close()

arquivo = open('Arquivo.txt', 'r')
a = arquivo.read()
print(a)
arquivo.close()


