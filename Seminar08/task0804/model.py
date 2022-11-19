hidden_word = ''
knownChars = set()
initialized = False


def init():
    global initialized
    f = open('db/data.txt', 'a')
    f.close()

    set_word("ПИТОНПИТОНПИТОНПИТОНПИТОНПИТОНПИТОН")
    knownChars.clear()

    initialized = True


def set_word(w):
    global hidden_word
    hidden_word = w


def get_word():
    if not initialized:
        init()

    return hidden_word


def add_knownChars(c: str):
    knownChars.add(c)
    return knownChars


def get_knownChars():
    if not initialized:
        init()

    return knownChars


def get_current_word_state():
    w = get_word()
    print(w)
    unknown = set(get_word())-get_knownChars()
    for c in unknown:
        w = w.replace(c, '*')
    return w


def encrypt_word():
    pass


def decrypt_word():
    pass


def add_char(c: str):
    add_knownChars(c)
    print(c)
    print(get_knownChars())


def is_game_end():
    return False
