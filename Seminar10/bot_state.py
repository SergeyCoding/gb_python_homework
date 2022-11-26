import common

states = {1: "Введите Ваш вопрос",
          2: "Ваш запрос обрабатывается",
          3: "Ответ",
          0: "Вопрос закрыт"}


def get_current_state(user_id: int):
    if not is_question(user_id):
        return 1

    if not is_answer(user_id):
        return 2

    if is_answer_done(user_id):
        return 0

    return 3


def start_question(user_id):
    common.delete(user_id)
    return


def is_question(user_id: int):
    pass


def is_answer(user_id: int):
    pass


def is_answer_done(user_id: int):
    pass
