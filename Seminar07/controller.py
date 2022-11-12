import model
import view


def new():
    view.info("\nВвод нового контакта:")
    name = view.get_name()
    phone = view.get_phone()
    id = model.create(name, phone)
    view.info(f"Добавлен контакт с id={id}\n")
    return "continue"


def all():
    view.info("\nВывод всего справочника:")
    out_type = view.get_out_type()

    if out_type == "console":
        view.output_to_console()
    elif out_type == "html":
        view.output_to_html()
    elif out_type == "json":
        view.output_to_json()

    return "exit"
