import views
import model


def run():
    model.init()
    menu()


def menu():
    views.info("Вы хотите играть?")
    if(views.get_yes_no()):
        game()

    # views.info("Вы хотите добавить вопрос?")
    # if(views.get_yes_no()):
    #     views.info("Вопрос: ")
    #     return


def game():
    views.info("\nИгра началась:\n")
    views.question()

    while(True):
        views.show_current_word()
        с = views.get_char()
        model.add_char(с)

        if model.is_game_end():
            views.info("\nВы угадали!\n")
            views.show_current_word()
            exit()
