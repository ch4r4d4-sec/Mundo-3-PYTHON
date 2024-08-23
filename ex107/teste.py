
import moeda

p = float(input('Digite o preço : R$ '))
print(f'O aumento de 35% temos  R${p} é R${moeda.aumentar(p, 35)}')
print(f'O diminuir de 10% temos R${p} é R${moeda.diminuir(p, 10)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'A metade de R${p} é R${moeda.metade(p)}')
