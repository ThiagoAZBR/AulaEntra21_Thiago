#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação
a = 1
b = 2
c = 3
d = 4
e = 5
print(f''' 
    Digite o Número Respectivo a Opção que Deseja:

    {a} - Cadastrar Funcionário
    {b} - Listar Funcionários
    {c} - Editar Funcionário
    {d} - Deletar Funcionário
    {e} - Sair 
    ''')
option = int(input('R: '))
if option == a:
    a = input('\nNome do Funcionário a Cadastrar: ')
if option == b:
    print('\nNão Há funcionários Cadastrados Ainda')
if option == c:
    print('\nNão Há funcionários Para Editar Ainda')
if option == d:
    print('\nNão Há funcionários Para Deletar Ainda')
if option == e:
    pass
print('\n FIM')