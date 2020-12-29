# Crie as seguintes classes com suas determinadas carcteristicas
# ram, hd, processador

# Agora, crie a classe Placa_mae, que deve ser composta pelos 3 itens acima

# Por fim, utilizando herança, crie dispositivos que utilizam a placa mãe; 
# por exemplo: computador

# Dia 16 de Novembro De 2020
from datetime import date, datetime
from time import sleep

class Memoria_RAM:
    def __init__(self):
        self.marca = 'Kingston'
        self.desempenho = '8Gb'
        self.hrtz = '1300 Mhz'
    
    def detalhes_ram(self):
        print(f'Sou uma Memória Ram:\nMarca: {self.marca}\nDesempenho: {self.desempenho}\nVelocidade: {self.hrtz}\n')
    
class HardDisk:
    def __init__(self):
        self.marca = 'Seagate'
        self.gb = '2Tb'
        self.tipo = 'SATA'
    
    def detalhes_hd(self):
        print(f'Sou Um Hard Disk\nMarca: {self.marca}\nArmazenamento: {self.gb}\nTipo: {self.tipo}\n')

class Processador:
    def __init__(self):
        self.tipo = 'i7'
        self.marca = 'intel'
        self.velocidade = '3.7 GHz'
    
    def detalhes_processador(self):
        print(f'Sou Um Processador\nTipo: {self.tipo}\nMarca: {self.marca}\nVelocidade: {self.velocidade}\n')

class Placa_mae(Memoria_RAM, HardDisk, Processador):
    def __init__(self):
        pass
    
    def sou(self):
        print('Placa Mãe, o Corpo dos Dispositivos Que estão em Mim!\n')

class Celular(Placa_mae):
    def __init__(self):
        self.origem = 'Vim das minas de metais raros de países em guerra.\nLá crianças trabalham para grandes empresarios que vendem esses minérios a empresas montadoras de celular.\nQue Depois vendem a você, e você compra, financiando o trabalho infantil nas minas e a poluição do solo na mineração!\n"Obrigado Por Escolher Me Comprar :)"\n'
    
    def de_onde_vim(self):
        print(self.origem)
    
    def mandar_mensagem(self):
        mensagem = input('O que Deseja Enviar? \nR: ')
        print(f'\nVocê Enviou: {mensagem}\n')
    
    def olhar_relogio(self):
        tempo = datetime.now()
        print(tempo.strftime('%A - %B - %Y   %H:%M:%S'))

if __name__ == '__main__':
    me = Memoria_RAM()
    hd = HardDisk()
    pr = Processador()
    
    me.detalhes_ram()
    sleep(3)
    hd.detalhes_hd()
    sleep(3)
    pr.detalhes_processador()
    sleep(3)

    cel = Celular()

    cel.sou()
    sleep(3)
    cel.de_onde_vim()
    sleep(6)
    cel.mandar_mensagem()
    sleep(3)
    cel.olhar_relogio()
