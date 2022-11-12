import model


def info(text):
    print(text)


def get_name():
    return input("имя: ")


def get_phone():
    return input("тел: ")


def get_out_type():
    out_type = {"1": "console", "2": "html", "3": "json"}
    lst = ', '.join(list(f"{k}-{v}" for k, v in out_type.items()))

    while True:
        k = input(lst+" > ")
        if k in out_type:
            return out_type[k]


def output_to(pre: str, fun, post: str):
    result = pre
    for item in model.get_store():
        result += fun(item)
    result += post

    return result


def output_to_console():
    for k, v in model.get_store().items():
        print(f" {k}\t{v}")


def output_to_html():
    htmlBegin = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style >
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
    }
    </style>
</head>
<body>
    <h1>Телефоны</h1>

    <table style="width:30%">
        <tr>
            <th>ID</th>
            <th>name</th>
            <th>phone</th>
        </tr>
"""
    htmlEnd = """
</table>
</body>
</html>
"""

    lst = list(f"""
<tr>
    <td>{k}</td>
    <td>{v[0]}</td>
    <td>{v[1]}</td>
<tr>
""" for k, v in model.get_store().items())

    f = open("./data/phone.html", "w", encoding="utf-8")
    f.writelines(htmlBegin+''.join(lst)+htmlEnd)
    f.close()


def output_to_json():
    jsonBegin = '{ "phones":['
    jsonEnd = "]}"

    lst = list(
        f'{{"id":{k}, "name":"{v[0]}", "phone":"{v[1]}" }}' for k, v in model.get_store().items())

    f = open("./data/phone.json", "w", encoding="utf-8")
    f.writelines(jsonBegin+','.join(lst)+jsonEnd)
    f.close()
