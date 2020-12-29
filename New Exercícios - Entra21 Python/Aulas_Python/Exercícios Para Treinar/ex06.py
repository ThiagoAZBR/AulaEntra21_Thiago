# Crie uma lista com todas as letras do alfabeto

# Remova as vogais dessa lista e crie uma tupla com elas

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro favorito

alfabeto = input('Digite: ').split(' ')

print(alfabeto)

var = alfabeto.pop(0), alfabeto.pop(3), alfabeto.pop(6), alfabeto.pop(11), alfabeto.pop(16)
print(var)
tupla = tuple(var)

nome = alfabeto[15], alfabeto[5], tupla[2], tupla[0], alfabeto[4], tupla[3]
nome = set(nome)

print(var)
print(nome)

idade = input('Qual A sua Idade? \n R: ')
livro = input('Qual Seu Livro Favorito \n R: ')

nome.add(idade)
nome.add(livro)
print(nome)
