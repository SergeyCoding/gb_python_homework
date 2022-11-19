# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год.
# Каждому месяцу соответствует своя строка. Определите самый жаркий и самый холодный 7-дневный промежуток этого периода.
# Выведите его даты.

# Задача 2. Дана квадратная матрица, заполненная случайными числами.
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random
import datetime
import calendar


def generate_temperature():
    return random.randint(-10, 33)


def generate_month(n: int):
    days = calendar.monthrange(datetime.datetime.today().year-1, n)[1]
    return list(generate_temperature() for _ in range(days))


def gen_period(m1, m2):
    result = dict()
    for m in range(m1, m2+1):
        result[m] = generate_month(m)
    return result


def print_period(period: dict):
    print("\nТемпературы по месяцам:")
    for k, v in period.items():
        print(f"{k} - \t{v}")


def get_date(month: int, days: int):
    '''
     дата через days дней от начала month-ого месяца прошлого года
    '''
    d1 = datetime.datetime(datetime.datetime.today().year-1, month, 1)

    return d1 + datetime.timedelta(days=days)


print("Семинар 8. Задача 3")

for_count_days = 7

p = gen_period(5, 9)
print_period(p)

days = list(item for sublist in (m for m in p.values()) for item in sublist)
print("\nТемпературы по дням:")
print(days)


t_for_7days = list(sum(days[i:i+for_count_days])
                   for i in range(len(days)-for_count_days+1))
print(t_for_7days)

nday_hot = t_for_7days.index(max(t_for_7days))
nday_cold = t_for_7days.index(min(t_for_7days))

print("\nЖаркий период: ", end='')
print(f"{get_date(5, nday_hot)} - {get_date(5, nday_hot - 1+for_count_days)}")
print("Холодный период: ", end='')
print(f"{get_date(5, nday_cold)} - {get_date(5, nday_cold - 1+for_count_days)}")
