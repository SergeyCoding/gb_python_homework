import common

states = {'wait': "Введите Ваш вопрос",
          'process': "Ваш запрос обрабатывается",
          'answer': "Ответ",
          'done': "Вопрос закрыт"}


def get_current_state(user_id: int):
    return common.get_state(user_id)


def set_current_state(user_id: int, state: str):
    common.set_state(user_id, state)


def start_question(user_id):
    common.delete_question(user_id)
    common.set_state(user_id, 'wait')
    return


def set_question(curUser: int, question: str):
    common.set_state(curUser, 'process')
    common.create_question(curUser, question)
    return


def done_question(user_id):
    common.set_state(user_id, 'done')
    return


def is_question(user_id: int):
    pass


def is_answer(user_id: int):
    pass


def is_answer_done(user_id: int):
    pass
