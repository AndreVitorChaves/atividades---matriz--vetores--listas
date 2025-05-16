def main():
    temperaturas = {
        "Domingo": 27.0,
        "Segunda": 30.0,
        "Terça": 27.6,
        "Quarta": 23.5,
        "Quinta": 29.3,
        "Sexta": 24.0,
        "Sábado": 21.0
    }

    menor = min(temperaturas.values())
    maior = max(temperaturas.values())

    print(f"A menor temperatura identificada foi: {menor:.2f}")
    print(f"A maior temperatura identificada foi: {maior:.2f}")

if __name__ == "__main__":
    main()
