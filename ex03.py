def main():
    
    temp = []

    
    for semana in range(3):
        semana_temps = []
        for dia in range(7):
            temperatura = float(input(f"Digite a temperatura do dia {dia + 1} da semana {semana + 1}: "))
            semana_temps.append(temperatura)
        temp.append(semana_temps)

  
    todas_temperaturas = [t for semana in temp for t in semana]

    menor = min(todas_temperaturas)
    maior = max(todas_temperaturas)
    media = sum(todas_temperaturas) / len(todas_temperaturas)

    print(f"\nA menor temperatura identificada foi: {menor:.2f}")
    print(f"A maior temperatura identificada foi: {maior:.2f}")
    print(f"\nTemperaturas abaixo da média ({media:.2f}):")

    
    for i, semana in enumerate(temp):
        for j, temperatura in enumerate(semana):
            if temperatura < media:
                print(f"Semana {i + 1}, Dia {j + 1}: {temperatura:.2f}")

if __name__ == "__main__":
    main()
