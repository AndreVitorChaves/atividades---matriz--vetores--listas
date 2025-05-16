temp = {'Segunda':27, 'Terça': 30, 'Quarta': 27.6, 'Quinta': 23.5, 'Sexta': 29.3, 'Sábado':  24, 'Domingo': 21}
media = sum(temp.values()) / len(temp)
for dia, valor in temp.items():
    if (valor < media):
        print(f'Menor que média: {dia}: {valor}')

