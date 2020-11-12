class Pessoa:

    def __init__(self, id, nome, cpf, email, endereco, data_nasc, telefone, pergunta_secreta, resposta, senha, letras_secretas):
        self.id = id
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.pergunta_secreta = pergunta_secreta
        self.resposta = resposta
        self.senha = senha
        self.letras_secretas = letras_secretas


    def __str__(self):
        return f"{self.id}_{self.nome}_{self.data_nasc}_{self.cpf}_{self.email}_{self.telefone}_{self.endereco}_{pergunta_secreta}_{resposta}_{senha}_{letras_secretas}"
