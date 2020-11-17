# Crie uma classa arco, com as caracteristicas básicas de um arco
# Utilizando herança, crie pelo menos mais 3 classes de arco com suas respectivas caracteristicas

# Referências
# https://gearjunkie.com/archery-bow-types-hunting-bowhunting
# https://scottisharchery.org.uk/get-started/archery-bow-types

# Super Bonus: Crie uma classe para cada parte do arco e altere a classe pai arco, utilizando cada parte para cria-la

'''                                         BÔNUS                                                   '''

from random import randint
from time import sleep

# Dia 15 de Novembro De 2020

class Arco:

    def __init__(self):
        self.empunhadura = 'Empunhadura do Arco'
        self.linha_arco = 'Linha Do Arco'
        self.lamina = 'Lamina do Arco'
        self.material = 'Madeira e Fibra de Taquara'
        self.tamanho = '152 cm'

    def por_flecha(self):
        print('Colocando a Flecha...')
    
    def mirar(self):
        print('Estabilizando O Arco para Atirar...')
    
    def puxar_corda(self):
        print('Puxando a A flecha...')

    def atirar(self):
        print('Soltando a Flecha No Alvo!')

    def acertou_errou(self):
        lista = ['Acertou!', 'Errou!']
        print(lista[randint(0,1)])

class Arco_Recurvo(Arco):
    def __init__(self):
        self.material = 'Metal ou Fibras'
        self.tamanho = '165 cm'
        self.personalido = 'Pode Ser personalizado'

class Arco_composto(Arco):
    def __init__(self):
        self.polias = 'Polias/roldanas'
        self.tamanho = '118 cm'
        self.personalido = 'Pode Ser Personalizado'
        self.material = 'Metal ou Fibras'

class Balestra(Arco):
    def __init__(self):
        self.tamanho = '90 cm'
        self.material = 'Metal ou Fibras'
        self.gatilho = 'Gatilho da balestra'
    
    def mirar(self):
        print('Estabilizando a Balestra para atirar...')
    
    def atirar(self):
        print('Apertou o gatilho!')

if __name__ == '__main__':
    a = Arco()
    a1 = Arco_Recurvo()
    a2 = Arco_composto()
    a3 = Balestra()


    a3.por_flecha()
    sleep(2)
    a3.puxar_corda()
    sleep(2)
    a3.mirar()
    sleep(2)
    a3.atirar()
    sleep(2)
    a3.acertou_errou()

