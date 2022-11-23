import game
import calc

GAME = 'game'
CALC = 'calc'
DIALOG = 'dialog'

current_state = DIALOG


def change_state(state: str):
    global current_state

    if state == GAME:
        game.init()
        current_state = state

    if state == CALC:
        current_state = CALC

    return


def inProcess(answer: str):
    global current_state
    if current_state == DIALOG:
        return []
    if current_state == CALC:
        return [calc.evalute(answer)]
    if current_state == GAME:

        try:
            num = int(answer)
        except:
            return ["???"]

        result = game.check(num)
        if not game.game_in_process:
            current_state = DIALOG
        return [result]
