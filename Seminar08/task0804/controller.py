import views
import model


def run():
    menu()


def menu():
    views.info("Вы хотите добавить вопрос?")
    if(views.get_yes_no()):
        pass
    else:
        views.info("Вы хотите играть?")
        if(views.get_yes_no()):
            game()


def game():
    views.info("\nИгра началась:")

    while(True):
        views.show_current_word()
        с = views.get_char()
        model.add_char(с)

        if model.is_game_end():
            views.info("Вы угадали!")
            exit()
