# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print("Семинар 2. Задача 1")

print(f"X\tY\tZ\tnot(X and Y) or Z")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f"{x}\t{y}\t{z}\t{int(not(x and y) or z)}")
