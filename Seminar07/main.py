# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# Предусмотрите следующие функции для справочника:
# - новая запись;
# - вывод всего справочника;
# - поиск по имени;
# - экспорт справочника в форматы html, xml;
# - чтение данных из файла;
# - дополнительные функции по желанию
# Требуется реализовать минимум 3 инструмента для работы со справочником.

import controller


def init():
    f = open("./data/phone.dat", mode="a")
    f.close()


init()


commands = {
    "new": ("Добавить новую запись", controller.new),
    "all": ("Вывод всего справочника", controller.all),
    "exit": ("Выйти",)}

while True:
    print("Выберите команду:")
    for k, v in commands.items():
        print(f"{k}\t- {v[0]}")

    cmd = input("> ").strip().lower()

    if cmd == "exit":
        exit()

    if cmd not in commands:
        print("нет такой команды", end='')
        input()
        print()
        continue

    response = commands[cmd][1]()

    if response == "exit":
        print("\nBuy")
        exit()
