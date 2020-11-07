'''                                                                      C H A M A D A  D E  C L A S S E S                                                                   '''

from ex09 import Caderno, Esmalte, Carteira, Mochila, Bola, Teclado, Garrafa, Computador, Mouse, Celular, Gato, Carro, Bicicleta
from time import sleep

sleep(1)
primeiro = Caderno('90', 'Preto', '1')
print(primeiro)

sleep(3)
# Até o Celular, são preços o último parâmetro.
# Até garrafa, é cor o primeiro.
# De Mouse até o Final, Cor também são o primeiro parâmetro
segundo = Esmalte('vermelho', 10, 12) # ml, o do meio
print(segundo)
sleep(3)

terceiro = Carteira('marrom', 3, 20) # Compartimentos, é o do meio.
print(terceiro)
sleep(3)

quarto = Mochila('preta', 30, 70) # Peso, é o do Meio.
print(quarto)
sleep(3)

quinto = Bola('branca', 'Futsal', 80) # Tipo, é o do meio .
print(quinto)
sleep(5)

sexto = Teclado('Azul e Preto', 'Com Fio',26) # Tipo, é o do meio.
print(sexto)
sleep(3)

setimo = Garrafa('verde', 'plastico', 10) # Material, é o do meio.
print(setimo)
sleep(3)

oitavo = Computador('3080', 8, 7.899) # Placa é o 1°, gb é o 2° e preço o 3°.
print(oitavo)
sleep(3)

nono = Mouse('Vermelho Com Preto', 'Com Fio', 30) # Tipo, é o do meio.
print(nono)
sleep(3)

decimo = Celular('Azul', 'Samsung', 799) # Marca é o do meio.
print(decimo)
sleep(5)

decimo_primeiro = Gato('Siamês', 'Rogério', 5) # Cor é o 1°, nome é o 2° e idade é o 3°
print(decimo_primeiro)
sleep(3)

decimo_segundo = Carro('Cinza', 'BMW', 120000) # Marca é o do meio
print(decimo_segundo)
sleep(3)

decimo_terceiro = Bicicleta('Laranja', 'Kaloi', 500) # Marca é o do Meio
print(decimo_terceiro)
