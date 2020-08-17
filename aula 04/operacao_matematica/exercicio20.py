#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

dinheiro_emprestado = float(input('Qual O Valor que deseja emprestado? '))
taxa_juros = float(input('Qual O Valor do Juros que deseja?'))
tempo_emprestimo = int(input('Quanto tempo deseja para pagar? '))


valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo

print(f'O Valor que será emprestado será de R$:{dinheiro_emprestado}, e a taxa de juros será {taxa_juros}%, o tempo para pagar será de {tempo_emprestimo} mês(es), e o valor a ser devolvido R$:{valor_receber}')