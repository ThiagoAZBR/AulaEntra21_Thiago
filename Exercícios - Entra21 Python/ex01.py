#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante
nome = input('Primeiro Nome: ')
sobrenome = input('Sobrenome: ')
cpf = int(input('CPF: '))
rg = int(input('RG: '))
salario = float(input('Salário Bruto: R$: '))
print(f'''
    Primeiro Nome:  {nome}
    Sobrenome:      {sobrenome} 
    CPF:            {cpf}
    RG:             {rg}
    Salário Bruto:  R$: {salario}''' )
