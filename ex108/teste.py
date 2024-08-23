import moeda2

p = float(input('Digite o preço : R$ '))
print(f'O aumento de 35% temos  {moeda2.moeda(p)} é {moeda2.moeda(moeda2.aumentar(p, 35))}')
print(f'O diminuir de 10% temos {moeda2.moeda(p)} é {moeda2.moeda(moeda2.diminuir(p, 10))}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.dobro(p))}')
print(f'A metade de {moeda2.moeda(p)} é {moeda2.moeda(moeda2.metade(p))}')