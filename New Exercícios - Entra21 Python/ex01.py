from datetime import date

today = str(date.today())
today = today.split('-')
today = int(today[0])

ano = int(input('Digite O Ano De Nascimento: '))

def calculo_idade(ano):
    calculo = today - ano
    var = '\nO Professor Tem ' + str(calculo) + ' Anos! \n'
    return var

print(calculo_idade(ano))
