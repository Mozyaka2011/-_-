def calculate_mass_fraction(solutions):
    total_mass_solution = 0
    total_mass_substance = 0

    for mass, concentration in solutions:
        mass_substance = mass * (concentration / 100)
        total_mass_solution += mass
        total_mass_substance += mass_substance

    if total_mass_solution == 0:
        return 0

    mass_fraction = (total_mass_substance / total_mass_solution) * 100
    return mass_fraction

def main():
    solutions = []
    while True:
        try:
            mass = float(input("Введите массу раствора (г) или '0' для завершения: "))
            if mass == 0:
                break
            concentration = float(input("Введите концентрацию раствора (%): "))
            solutions.append((mass, concentration))
        except ValueError:
            print("Пожалуйста, введите корректные числовые значения.")

    mass_fraction = calculate_mass_fraction(solutions)
    print(f"Массовая доля вещества в смешанном растворе: {mass_fraction:.2f}%")

if __name__ == "__main__":
    main()
