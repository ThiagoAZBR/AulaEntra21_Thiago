#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter 
#--- resultado esperado: -------------- Cadastro Serasa --------------------------
#--- O cabeçalho deve conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa
'''                                         Aula de Funções                                                         '''


def introduction():
    company = 'T - Systems'
    print(15 * '-=' + '-', 'Cadastro', company, 15 * '-=' + '-')

introduction()