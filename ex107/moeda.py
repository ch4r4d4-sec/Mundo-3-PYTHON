#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). F
#aça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preco, taxa):
   res = preco + (preco * taxa/100)
   return res

def diminuir(preco, taxa):
   res = preco - (preco * taxa/100)
   return res

def dobro(preco):
   res = preco * 2
   return res

def metade(preco):
   res = preco / 2
   return res