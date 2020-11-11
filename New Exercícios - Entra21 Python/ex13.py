class Pessoas:

    def __init__(self, nome, idade, cpf):

        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def nombre(self):
        print(f'Nome: {self.nome}')
    
    def age(self):
        print(f'Idade: {self.idade}')

    def CPF(self):
        print(f'CPF: {self.cpf}')
    
    def __str__(self):
        return f'{self.nome} - {self.idade} - {self.cpf} |'
