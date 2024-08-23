# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 15) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze')

while True:
    num = int(input('Digite um número entre 0 e 15: '))
    if 0 <= num <= 15:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número \033[32m{cont[num]}\033[m')