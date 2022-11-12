telephones = dict()
initialized = False


def init():
    f = open("./data/phone.dat", "r", encoding="utf-8")
    while True:
        ln = f.readline()
        if ln == "":
            break

        ln = ln.strip().split("<|>")

        telephones[int(ln[0])] = (ln[1], ln[2])
    f.close()


def get_store():
    if not initialized:
        init()

    return telephones


def create(name: str, phone: str):
    id = 0
    if len(get_store()) > 0:
        id = max(get_store().keys())+1
    get_store()[id] = (name, phone)

    f = open("./data/phone.dat", "a", encoding='utf-8')
    f.write(f"\n{id}<|>{name}<|>{phone}")
    f.close()

    return id


def find_by_name(name: str):
    return filter(lambda x: x[0] == name, get_store())
