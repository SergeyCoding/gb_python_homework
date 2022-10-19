# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# Результат: 8x^2 + 4x + 8


def read_polynom(file_name):
    f = open(file_name, mode="r", encoding="utf-8")
    s_polynom = (
        f.readline()
        .strip()
        .replace(" ", "")
        .replace("+", "|+")
        .replace("-", "|-")
        .replace("+x", "+1x")
        .replace("-x", "-1x")
        .replace("x^", "&")
        .replace("x", "&1")
    )
    result = dict()
    for p in s_polynom.split("|"):
        if "&" in p:
            pp = p.split("&")
            result[int(pp[1])] = int(pp[0])
        else:
            result[0] = int(p)

    f.close()
    return result


def sum_polynoms(pol1, pol2):
    factors = set(pol1).union(set(pol2))
    result = dict()
    for f in factors:
        result[f] = (pol1[f] if f in pol1 else 0)+(pol2[f] if f in pol2 else 0)
    return result


def print_polynom(polynom):
    lst = list(polynom)
    lst.sort(reverse=True)

    first = True
    for f in lst:
        p = abs(polynom[f])
        if not first or polynom[f] < 0:
            print(f" {'+' if polynom[f]>=0 else '-'} ", end="")
        if f == 0:
            print(f"{p}", end="")
        if f == 1:
            print(f"{p if p!=1 else ''}x", end="")
        if f > 1:
            print(f"{p if p!=1 else ''}x^{f}", end="")
        first = False
    print()


polynom1 = read_polynom("data0404a.txt")
polynom2 = read_polynom("data0404b.txt")

res = sum_polynoms(polynom1, polynom2)
print_polynom(res)
