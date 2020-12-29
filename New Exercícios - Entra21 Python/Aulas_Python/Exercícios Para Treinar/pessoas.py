class Pessoa:

    def __init__(self, nome, cpf, email, endereco, data_nasc, telefone):
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco


    def __str__(self):
        return f"{self.id} | {self.nome} | {self.data_nasc} | {self.cpf} | {self.email} | {self.telefone} | {self.endereco} |"

class Conta_Banco:
    
    def __init__(self,cpf, numconta, pergunta_secreta, resposta, senha, letras_secretas):
        self.pergunta_secreta = pergunta_secreta
        self.resposta = resposta
        self.senha = senha
        self.letras_secretas = letras_secretas
        self.numconta = numconta
        self.cpf = cpf
        self.numconta = numconta
    
    def __str__(self):
        return f'{self.cpf} | {self.pergunta_secreta} | {self.resposta} | {self.senha} | {self.letras_secretas} | {numconta}'
