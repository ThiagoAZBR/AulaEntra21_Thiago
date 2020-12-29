# 10/11

# Construa uma classe chamada veiculo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)


from ex13 import Pessoas
lista = []
person = []

class Veiculo:

    passageiro = []
    def __init__(self, cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa):

        self.rodas = rodas
        self.cor = cor
        self.onde_se_locomove = onde_se_locomove
        self.quant_pessoas = quant_pessoas
        self.portas = portas    

    def coloracao(self):
        print(f'A Cor do Seu Veiculo é {self.cor}!')

    def mover(self):
        print(f'Se Move por {self.onde_se_locomove}')
    
    def carregar(self):
        print(f'Carrega Um Tanto de {self.quant_pessoas} pessoas ')
    
    def ter_ou_nao(self):
        print(f'{self.rodas}Tem Rodas!')

    def aberto_fechado(self):
        print(f'{self.portas}Tem Portas!')
    
    def addpersona(self, variavel):
        lista.append(variavel)

    def removepersona(self, variavel):
        lista.remove(variavel)

    

    print(lista)

class Moto(Veiculo):

    def __init__(self, cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa):
        super().__init__(cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa)

class Navio(Veiculo):

    def __init__(self, cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa):
        super().__init__(cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa)
    
class Aviao(Veiculo):

    def __init__(self, cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa):
        super().__init__(cor, onde_se_locomove, quant_pessoas, portas, rodas, pessoa)
    

if __name__ == "__main__":

    while True:

        a = input('Nome: ')
        b = int(input('Idade: '))
        c = int(input('CPF: '))

        person.append(a)
        person.append(b)
        person.append(c)

        p4 = Pessoas(person[0], person[1], person[2])
        option = input('Deseja Continuar?\n R: ').upper()
        if option == 'SIM' or option == 'S':
            pass
        else:
            break
    
    p1 = Pessoas("Bruno", 29, 1234567)
    p2 = Pessoas('Heindall', 29, 4583765738)
    v = Veiculo('','','','','','')

    v.addpersona(p1)
    v.addpersona(p2)
    v.addpersona(p4)
    print(*lista)

    v.removepersona(p1)

    print(*lista)
    print('Aqui')
