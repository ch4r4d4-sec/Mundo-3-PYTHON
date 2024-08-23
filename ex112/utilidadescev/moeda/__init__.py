#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de 
#funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.

def aumentar(preco = 0, taxa = 0, formato = False):
   res = preco + (preco * taxa / 100)
   return res if formato is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formato = False):
   res = preco - (preco * taxa / 100)
   return res if formato is False else moeda(res)

def dobro(preco = 0, formato = False):
   res = preco * 2
   return res if not formato else moeda(res)

def metade(preco = 0, formato = False):
   res = preco / 2
   return res if not formato else moeda(res)

def moeda(preco = 0, moeda = 'R$ '):
   return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco = 0, taxaa = 10, taxar = 5):
   print('\033[0;33m-\033[m' * 30)
   print('\033[0;32mRESUMO DO VALOR\033[m'.center(30))
   print('\033[0;33m-\033[m' * 30)
   print(f'\033[0;36mPreço analisado:\033[m \t{moeda(preco)}')
   print(f'\033[0;36mDobro do preço:\033[m \t{dobro(preco, True)}')
   print(f'\033[0;36mMetade do preço:\033[m \t{metade(preco, True)}')
   print(f'\033[0;36m{taxaa}% de aumento:\033[m \t{aumentar(preco, taxaa, True)}')
   print(f'\033[0;36m{taxar}% de redução:\033[m \t{diminuir(preco, taxar, True)}')
   print('\033[0;33m-\033[m' * 30)