# Crie uma classe chamada Mario; ele terá inicialmente um atributo power que estará vazio, e dois métodos: jump e use_power
# Utilizando Herança, crie ao menos 5 classes que representará os power ups de mario
# Exemplo: classe fire_flower: o metodo use_power retornara uma bola de fogo!!!
# Obs: Cada power up, muda determinadas caracteristicas do personagem, você pode implementa-las também :D

# Super Bonus: Faça um menu que nos permita testar os poderes do Mario :D
# Referencia: https://www.mariowiki.com/List_of_power-ups 

# Hyper Bonus: faça uma classe inimigo; utilizando herença construa classes como goomba, koopa, bowser;
# Ultra Hyper Super Mega Bonus: faça tudo isso iteragir de alguma forma via console =D

class Mario:
    def __init__(self):
        self.power = 'No Power'
        self.vida = '1 vida'

    def jump(self):
        print('Pulo!')
    def use_power(self):
        print('No Power')

class grow_up(Mario):
    def __init__(self):
        self.vidaextra = '+1 vida'
    
    def adquirir_vida(self):
        print(f'{self.vidaextra} Adquirida!')

class flor_de_fogo(self):
    def __init__(self):
        self.firepower = 'Poder De Fogo'
    def use_power(self):
        print('SOU EU BOLA DE FOGO O CALOR TA DE MATAR!')

class invencibilidade(self):
    def __init__(self):
        self.tocou_morreu = 'Invencivel!'
    
    def use_power(self):
        print('Invencibilidade Adquirida, Não tenha medo!')

