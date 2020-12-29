arquivo = open('teste.txt', 'a')
arquivo.write('1\n2\n5\n4\n')
arquivo.close()

arquivo = open('teste.txt', 'r')
quant = len(arquivo.readlines())
count = 0
print('algo')
for a in arquivo:
    print('Algo')
    linha_limpa = a.strip()
    lista = linha_limpa.split()
    print(count)
    count = count +1
    if '4' in lista:
        print('Achei')
        break
#    if count == quant:
#        print('Não Foi Encontrado')
#        break
print(count)
arquivo.close()