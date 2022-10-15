# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий


def create_datafile(file_name):

    f = open(file_name, mode='r+', encoding='utf-8')

    check_f = {"привет": "привет", 'как тебя зовут?': "Нафаня, а тебя?"}

    for line in f:
        if len(check_f) == 0:
            break
        for ch in set(check_f):
            if line.lower().startswith(ch):
                check_f.pop(ch)

    line = f.readline()
    while line != '' and len(check_set) > 0:
        for ch in check_set:
            if line.lower().startswith(ch):
                check_f.pop(ch)
        check_set = set(check_f)
        line = f.readline()

    if len(check_set) > 0:
        for ch in check_set:
            f.write(f"{ch}<|>{check_f[ch]}\n")

    f.close()


def add_phrase(datafile, question):
    print("###")
    print('Что обычно отвечают на эту фразу? ')
    answer = input("> ")

    f = open(datafile, mode='r+', encoding='utf-8')

    f.write(f"{question}<|>{answer}\n")

    f.close()

    print('###')


def speaking(datafile):
    while True:
        question = input("you> ")

        is_answer = False

        f = open(datafile, mode="r+", encoding='utf-8')

        for line in f:
            answer = line.split("<|>")
            if answer[0].lower() == question.lower():
                print(f"---> {answer[1]}")
                is_answer = True

        f.close

        if not is_answer:
            add_phrase(datafile, question)


file_name = "data0303.txt"

f = open(file_name, mode='a', encoding='utf-8')
f.close()

create_datafile(file_name)
speaking(file_name)
