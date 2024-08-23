#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
#informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


def aumentar(preco = 0, taxa = 0):
   res = preco + (preco * taxa/100)
   return res

def diminuir(preco = 0, taxa = 0):
   res = preco - (preco * taxa/100)
   return res

def dobro(preco = 0):
   res = preco * 2
   return res

def metade(preco = 0):
   res = preco / 2
   return res

def moeda(preco = 0, moeda = 'R$ '):
   return f'{moeda}{preco:.2f}'.replace('.', ',')