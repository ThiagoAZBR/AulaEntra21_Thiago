#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro
titulo = "Harry Potter And The SORCERER'S STONE"
edtion = 'SCHOLASTIC, 1° Edição'
autora = 'J.K. Rowling'
data_de_publicacao = 1999
paragrafos = ''' 
                The ancient study of  alchemy  is  concerned  with  mak-
                ing the Sorcerer's Stone, a legendary substance with as-
                tonishing powers. The  Stone  will  transform any metal
                into pure gold. It also produces the  Elixir  of  Life,
                which will make the drinker immortal.
                    There have  been  many  reports  of  the Sorcerer's
                Stone over  the centuries, but the only Stone currently
                in  existence  belongs to Mr. Nicolas Flamel, the noted
                alchemist  and  opera  lover.  Mr.  Flamel,  who  cele-
                brated  his  six  hundred and sixty-fifth birthday last
                year,  enjoys  a  quiet  life  in  Devon with his wife,
                Perenelle(six hundred and fifty-eight).'''
print(f''' 
    A Seguir, 2 Parágrafos do Último Livro que Li:

    {paragrafos}


    Título:              {titulo}
    Edição:              {edtion}
    Autor(a):            {autora}
    Data de Publicação:  {data_de_publicacao} ''')