
import moeda

p = float(input('Digite o preço : R$ '))
print(f'O aumento de 35% temos  {moeda.moeda(p)} é {moeda.aumentar(p, 35, True)}')
print(f'O diminuir de 10% temos {moeda.moeda(p)} é {moeda.diminuir(p, 10, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')

