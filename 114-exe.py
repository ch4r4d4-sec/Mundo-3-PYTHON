#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.error
import urllib.request

try:
   site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
   print('O site Pudim não está acessível no momento.')
else:
   print('Consegui acessar o site Pudim com sucesso!')
   print(site.read())