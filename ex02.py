temp = {27, 30, 27.6, 23.5, 29.3, 24, 21}
media = sum(temp)/len(temp)
for c, valor in enumerate(temp):
    if valor < media:
        match(c):
            case 0:
                print(f'A temperatuda de domingo abaixo da média: {valor}: ')
            case 1: 
                print(f'A temperatuda de segunda-feira abaixo da média: {valor} ')
            case 2:
                print(f'A temperatuda de terça-feira abaixo da média: {valor} ')
            case 3:
                print(f'A temperatuda de quarta-feira abaixo da média: {valor} ')
            case 4:
                print(f'A temperatuda de quinta-feira abaixo da média: {valor} ')
            case 5:
                print(f'A temperatuda de sexta-feira abaixo da média: {valor} ')
            case 6:
                print(f'A temperatuda de sábado abaixo da média: {valor} ')
