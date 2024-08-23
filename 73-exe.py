#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Águia de Marabá', 'Aimoré', 'Altos', 'América-MG', 'América-PE', 'América-RN',
         'Anapolina', 'Anápolis', 'Aparecidense', 'Ariquemes', 'ASA', 'Athletic', 'Athletico Paranaense',
         'Atlético Acreano', 'Atlético Cearense', 'Atlético De Alagoinhas', 'Atlético Goianiense', 
         'Avenida', 'Bahia', 'Brasiliense', 'Chapecoense', 'Camburiú', 'Campinense', 'Caxias')

print('-=' * 15)
print(f'Lista de times do brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}° posição')


