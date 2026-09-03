while True:
    week = 7  # days in a week
    cig_per_day = 1  # assuming smoking just 1 cigarette a day
    cig_pack = 20  # cigarettes in a pack

    try:
        x = float(input("Choose how many weeks: "))
        total_days = week * x  # total days based on weeks chosen
        total_cigarettes = total_days * cig_per_day  # total cigarettes smoked
        packs_needed = total_cigarettes / cig_pack  # packs needed

        print(f"Total days: {total_days} days")
        print(f"Total cigarettes smoked: {total_cigarettes} cigarettes")
        print(f"Packs needed: {packs_needed:.2f} packs")
    except ValueError:
        print("Please enter a valid number.")