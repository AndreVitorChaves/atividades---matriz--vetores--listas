def main():
    dias_semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    temperaturas = {
        "Semana 1": {},
        "Semana 2": {},
        "Semana 3": {}
    }

    
    for semana in temperaturas.keys():
        print(f"Insira as temperaturas para {semana}:")
        for dia in dias_semana:
            while True:
                try:
                    temp = float(input(f"Temperatura do {dia}: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número válido.")
            temperaturas[semana][dia] = temp

    
    todas_temperaturas = []
    for semana in temperaturas.values():
        todas_temperaturas.extend(semana.values())

    menor = min(todas_temperaturas)
    maior = max(todas_temperaturas)
    media = sum(todas_temperaturas) / len(todas_temperaturas)

    print(f"\nA menor temperatura identificada foi: {menor:.2f}")
    print(f"A maior temperatura identificada foi: {maior:.2f}")
    print(f"\nTemperaturas abaixo da média ({media:.2f}):")

    
    for nome_semana, dias in temperaturas.items():
        for dia, temp in dias.items():
            if temp < media:
                print(f"{nome_semana} - {dia}: {temp:.2f}")

if __name__ == "__main__":
    main()
