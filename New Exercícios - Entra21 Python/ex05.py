arquivo = open('teste.txt', 'w')
arquivo.write('1')
arquivo.write('\n3 jfsjfjshgs')
arquivo.close()

arquivo = open('teste.txt', 'r')
for a in arquivo:
    linha_limpa = a.strip()
    lista = linha_limpa.split()
    if '3' in lista:
        print(a)
    else:
        print('erro')
arquivo.close()