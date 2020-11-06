'''                                                            FORMAÇÂO DE CLASSES                                                                                                 '''

class Caderno:

    marca = 'Tilibra'

    def __init__(self, pag, cor, materia):

        self.pag = pag
        self.cor = cor
        self.materia = materia

    def __str__(self):
        return f'\nO Caderno Tem {self.pag} páginas, e a cor {self.cor}, é um caderno de {self.materia} matéria(s)\n'

class Esmalte:

    marca = 'Risqué'

    def __init__(self, cor, ml, preço):

        self.cor = cor
        self.ml = ml
        self.preço = preço

    def __str__(self):
        return f'O Esmalte é da cor {self.cor}, contém {self.ml} ml(s), e custa R$: {self.preço:.2f}\n'

class Carteira:

    tipo = 'Couro'

    def __init__(self, cor, preço, compartimentos):

        self.cor = cor
        self.preço = preço
        self.compartimentos = compartimentos
    
    def __str__(self):
        return f'A cor da Carteira é {self.cor}, tem {self.compartimentos} compartimentos, e Custa R$: {self.preço}\n'

class Mochila:

    tipo = 'Sem Rodinhas'

    def __init__(self, cor, preço, peso):

        self.cor = cor
        self.preço = preço
        self.peso = peso
    
    def __str__(self):
        return f'A Cor da Mochila é {self.cor}, aguenta o peso de {self.peso}, e Custa {self.preço}\n'

class Bola:

    marca = 'Nike'

    def __init__(self, cor, tipo, preço):

        self.cor = cor
        self.tipo = tipo
        self.preço = preço
    
    def __str__(self):
        return f'A cor da bola é {self.cor}, e é feito para {self.tipo}, tem o preço de {self.preço}'

class Teclado:

    marca = 'logitech'

    def __init__(self, cor,tipo, preço):

        self.cor = cor
        self.tipo = tipo
        self.preço = preço
    
    def __str__(self):
        return f'A cor do Teclado é {self.cor}, ele é {self.tipo} tem o preço de R$: {self.preço}\n'

class Garrafa:

    tipo = 'Água'

    def __init__(self, cor,material, preço):

        self.cor = cor
        self.material = material
        self.preço = preço
    
    def __str__(self):
        return f'A cor da garrafa é {self.cor}, ele é feito de {self.material} tem o preço de R$: {self.preço}\n'

class Computador:

    tipo = 'De Casa'

    def __init__(self, placa, preço, gb):

        self.placa = placa
        self.gb = gb
        self.preço = preço
    
    def __str__(self):
        return f'A Placa do Computador é uma {self.placa}, tem {self.gb} Gb de RAm, e tem o preço de R$: {self.preço}\n'
    
class Mouse:

    marca = 'logitech'

    def __init__(self, cor, tipo, preço):

        self.cor = cor
        self.tipo = tipo
        self.preço = tipo
    
    def __str__(self):
        return f'A cor do Mouse é {self.cor}, é {self.tipo}, e tem o preço de R$: {self.preço}\n'
    
    class Celular:

        sistema = 'Android'

    def __init__(self, cor, marca, preço):

        self.cor = cor
        self.marca = marca
        self.preço = preço
    
    def __str__(self):
        return f'A cor do Celular é {self.cor}, e é da marca {self.marca}, tem o preço de R$: {self.preço}\n'

class Gato:

    tipo = 'Felis silvestris catus'

def __init__(self, cor, nome, idade):

    self.cor = cor
    self.nome = nome
    self.idade = idade

def __str__(self):
    return f'A cor do gato é {self.cor}, seu nome é {self.nome} tem a idade {self.idade} anos!\n'

class Carro:

    quant = '4 Pessoas'

def __init__(self, cor, marca, preço):

    self.cor = cor
    self.marca = marca
    self.preço = preço

def __str__(self):
    return f'A cor do Carro é {self.cor}, e da marca {self.marca}, tem o preço de R$: {self.preço}\n'

class bicicleta:

    para_o_que = 'Esporte'

def __init__(self, cor, marca, preço):

    self.cor = cor
    self.marca = marca
    self.preço = preço

def __str__(self):
    return f'A cor da Bicicleta é {self.cor}, e da marca {self.marca}, tem o preço de R$: {self.preço}\n'

class :

def __init__(self, cor, preço):

    self.cor = cor
    self.
    self.preço = preço

def __str__(self):
    return f'A cor do {self.cor} {self.} tem o preço de R$: {self.preço}\n'


