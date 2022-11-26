data_dir = "data/"
question_file = 'questions.dat'
answers_file = 'answers.dat'
state_file = 'state.dat'


def init_data():
    global data_dir

    f = open(data_dir+question_file, 'a')
    f.close()

    f = open(data_dir+answers_file, 'a')
    f.close()

    f = open(data_dir+state_file, 'a')
    f.close()


def create_question(user_id: int, question: str):
    f = open(data_dir+question_file, 'a', encoding='utf-8')
    f.write(f"{user_id} {question}\n")
    f.close()


def get_questions():
    id_list = []

    f = open(data_dir+question_file, 'r', encoding='utf-8')
    for line in f.readlines():
        id_list.append(line[:line.find(' ')])
    f.close()

    return id_list


def read_question(user_id: int):
    f = open(data_dir+question_file, 'r', encoding='utf-8')

    for line in f.readlines():
        pos = line.find(' ')
        if int(line[:pos]) == user_id:
            res = line[pos:]
            break
    f.close()

    return res


def delete_question(user_id):
    rewrite(data_dir+question_file, user_id)
    rewrite(data_dir+answers_file, user_id)
    rewrite(data_dir+state_file, user_id)


def rewrite(file_name: str, user_id: int):
    ll = []

    f = open(file_name, 'r', encoding='utf-8')
    for line in f.readlines():
        if line.startswith(str(user_id)):
            continue
        ll.append()
    f.close()

    f = open(file_name, 'w', encoding='utf-8')
    f.writelines(ll)
    f.close()


def create_answer(answer: str):
    pass


def read_answer(id: int, question: str):
    pass


def set_state(user_id: int, state: str):
    rewrite(data_dir+state_file, user_id)

    f = open(data_dir+state_file, 'a', encoding='utf-8')
    f.write(f'{user_id} {state}\n')
    f.close()


def get_state(user_id: int):
    f = open(data_dir+state_file, 'r', encoding='utf-8')

    for line in f.readlines():
        pos = line.find(' ')
        if int(line[:pos]) == user_id:
            res = line[pos:]
            break
    f.close()

    return res
