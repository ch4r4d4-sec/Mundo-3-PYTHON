#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas     – A maior nota   – A menor nota  
#  – A média da turma    – A situação (opcional)

def notas(*n, sit=False):
   """
   -> Função para analisar notas e situações de vários alunos.
   :PARAM n: uma ou mais notas dos alunos (aceita várias)
   :PARAM sit: valor opcional, indicando se deve ou não adicionar a situação 
   :RETURN: dicionário com várias informações sobre a situação da turma.

   """
   r = dict()
   r['total'] = len(n)
   r['maior'] = max(n)
   r['menor'] = min(n)
   r['media'] = sum(n) / len(n)
   if sit:
      if r['media'] >= 7:
         r['dituacao'] = 'BOA'
      elif r['media'] >= 5:
         r['situacao'] = 'RAZOÁVEL'
      else:
         r['situacao'] = 'RUIM'
   return r

resp = notas(6, 8.5, 9, sit=True)
print(resp)
#help(notas)