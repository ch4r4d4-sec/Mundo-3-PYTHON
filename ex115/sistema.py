#Vamos criar um menu em Python, usando modularização.

from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'ch4r4d4.txt'

if not arquivoExiste(arq):
   criarAquivo(arq)

while True:
   resposta = menu(['Ver pessoas cadastrada', 'Cadastrar nova Pessoas', 'Sair so Sistema'])
   if resposta == 1:
      lerArquivo(arq)
   elif resposta == 2:
      cabecalho('NOVO CADASTRO')
      nome = str(input('Nome: '))
      idade = leiaInt('Idade: ')
      cadastro(arq, nome, idade)
   elif resposta == 3:
      cabecalho('Saindo do sistema.. Até logo!')
      break
   else:
      print('\033[31mERRO! Digite uma opção válida!\033[m')
   sleep(0.6)