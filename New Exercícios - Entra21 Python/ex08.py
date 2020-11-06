from os import system, name 

palavra = None
chances = 0

def carregar_config():
    global palavra
    global chances
    linhas_arquivo = []
    with open('C:\\Users\\thiago.zeferino\\Desktop\\git professor _Entra21\\entra21\\aula1\\forca.cfg') as f:
        for linha in f:
            linhas_arquivo.append(linha.strip())
    palavra = str(linhas_arquivo[0])
    chances = int(linhas_arquivo[1])


arquivo = open('C:\\Users\\thiago.zeferino\\Desktop\\git professor _Entra21\\entra21\\aula1\\forca.cfg', 'r')
print('                                                             Começando...')

def limpar_tela():
# for windows 
    if name == 'nt': 
        system('cls') 
# for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear')

limpar_tela()

def jogar():
    global palavra # Diferente
    global chances
    carregar_config()
    letras_usadas = []
    
    


    while True:
        
        tentativa_palavra = ""
                

        print("Número de chances: %d - tentativas:" % chances) # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n\n\n\n")
        for x in palavra.strip():
            if x in letras_usadas:
                tentativa_palavra += x 
            else:
                 tentativa_palavra += "_"
                
        print(tentativa_palavra + "\n\n")

        if chances == 0:
            print("Você perdeu!")
            break
        if tentativa_palavra == palavra:
            print("Você ganhou com apenas %d" % chances + ' Chances!\n ')
            break
        chute = ""

        def prevenir():
            while True:
                
                chute = input("Digite uma letra: ") 
                if chute.isdigit() == True:
                    pass
                elif chute in letras_usadas:
                    print('Já Foi Usada!')
                    pass
                else: 
                    letras_usadas.append(chute)
                    break
        prevenir()
            
        
        
        if not chute in palavra:
            chances -= 1

        # temos um bug aqui =D   RESOLVIDO KK     



if __name__ == "__main__":
    # implementar a função carregar_config
    # implementar a função verifica_fim_jogo
    # implementar a função limpar_tela

    # previnir que o usuário digite números
    # previnir que o usuário repita letras

    # implementar menu de usuário com as seguintes opções:
    # 1 - Jogar
    # 2 - Modificar as configurações
    # 3 - sair
    
    # https://realpython.com/quizzes/python-dicts/viewer/

    jogar()
