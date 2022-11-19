hidden_word = [""]
knownChars = set()
isInitialized = False


def init():
    f = open('db/data.txt', 'a')
    f.close()

    set_word("ПИТОНПИТОНПИТОНПИТОНПИТОНПИТОНПИТОН")
    knownChars.clear()


def set_word(w):
    hidden_word[0] = w


def get_word():
    if not isInitialized:
        init()

    return hidden_word[0]


def get_knownChars():
    if not isInitialized:
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
    get_knownChars().add(c)


def is_game_end():
    return False
