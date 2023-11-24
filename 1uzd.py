lietotaja_ievade = int(input("Ievadiet skaitli: "))
summa = 0
for skaitlis in range(1, lietotaja_ievade + 1):
    summa += skaitlis
print(f"Summa no 1 līdz {lietotaja_ievade} ir: {summa}")