from ex11 import Moto
from ex11 import Navio
from ex11 import Aviao
from time import sleep

moto = Moto('Vermelho', 'Terra', 2, 'Não ', '', '')
navio = Navio('Preto', 'Mar', 400, '', 'Não ', '')
aviao = Aviao('Branco', 'Ar', 6, '', 'Não ', '')

print(f'\n{type(moto).__name__:^20}\n')
moto.coloracao()
moto.mover()
moto.carregar()
moto.aberto_fechado()
moto.ter_ou_nao()
sleep(6)
print(f'\n\n{type(navio).__name__:^20}\n')
navio.coloracao()
navio.mover()
navio.carregar()
navio.aberto_fechado()
navio.ter_ou_nao()
sleep(6)

print(f'\n\n{type(aviao).__name__:^20}\n')
aviao.coloracao()
aviao.mover() 
aviao.carregar()
aviao.aberto_fechado() 
aviao.ter_ou_nao()
