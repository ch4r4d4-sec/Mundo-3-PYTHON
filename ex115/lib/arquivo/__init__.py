# Vamos ver como fazer acesso a arquivos usando o Python.

from lib.interface import *


def arquivoExiste(nome):
   try:
      a = open(nome, 'rt')
      a.close
   except FileNotFoundError:
      return False
   else:
      return True
   

def criarAquivo(nome):
   try:
      a = open(nome, 'wt+')
      a.close
   except:
      print('Houve um \033[31mERRO\033[m na criação do arquivo!')
   else:
      print(f'Arquivo \033[32m{nome}\033[m criado com sucesso!')


def lerArquivo(nome):
   try:
      a = open(nome, 'rt')
   except:
      print('Erro ao ler o arquivo!')
   else:
      cabecalho('PESSOAS CADASTRADAS')
      for linha in a:
         dado = linha.split(';')
         dado[1] = dado[1].replace('\n', '')
         print(f'{dado[0]:<30}{dado[1]:>3} anos')
   finally:
      a.close()


def cadastro(arq, nome='desconhecido', idade=0):
   try:
      a = open(arq, 'at')
   except:
      print('Houve um ERRO na abertura do arquivo!')
   else:
      try:
         a.write(f'{nome};{idade}\n')
      except:
         print('Houve um ERRO na hora de escrever os dados!')
      else:
         print(f'Novo registro de {nome} adicionado.')
         a.close()