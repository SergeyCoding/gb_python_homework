# %% [markdown]
# ## Задача 2
# Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

# %%
import matplotlib.pyplot as plt
import numpy as np
from random import randint
houses_count = 15

cost_min = 3_000_000
cost_max = 20_000_000

square_min = 100
square_max = 300

# %%

houses_square = []
houses_cost = []

for i in range(houses_count):
    square = randint(square_min, square_max)
    houses_square.append(square)
    houses_cost.append(round(randint(cost_min, cost_max), -3))

# %%
max_cost_for_square = 50_000

houses = [(houses_square[i], houses_cost[i], round(
    houses_cost[i]/houses_square[i])) for i in range(len(houses_square))]

# %%

d = (square_max-square_min)/10
x = np.arange(square_min, square_max+d, d)


sp = plt.subplot(111)
plt.xlabel(r'Площадь дома, кв.м')
plt.ylabel(r'Стоимость 1 кв. м')
plt.title(r'Сведения о домах')
plt.grid(True)

bh = [*filter(lambda x:x[2] >= 50_000, houses)]
rh = [*filter(lambda x:x[2] < 50_000, houses)]
plt.plot([h[0] for h in bh], [h[2] for h in bh], 'bs')
plt.plot([h[0] for h in rh], [h[2] for h in rh], 'gs')
plt.plot(x, max_cost_for_square+0*x, 'r--')


rh.sort(key=lambda x: x[0])
for house in rh:
    print(
        f"Дом площадью {house[0]}, стоимость {house[1]}, стоимость за кв.м {house[2]}")

plt.show()
