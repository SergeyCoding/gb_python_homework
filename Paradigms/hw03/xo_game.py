"class XoGame"

import random

class XoGame:
    "Крестики-нолики"

    board_fld = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
    winner = ""

    def __init__(self):
        pass


    def check_line(self,line, ch):
        "check line"
        for (v, h) in line:
            if self.board_fld[v][h] != ch:
                return
        self.winner = ch



    def is_end_game(self):
        "is end game?"
        for v in range(3):
            self.check_line([(v, 0), (v, 1), (v, 2)], "X")
            self.check_line([(v, 0), (v, 1), (v, 2)], "O")

        for h in range(3):
            self.check_line([(0, h), (1, h), (2, h)], "X")
            self.check_line([(0, h), (1, h), (2, h)], "O")

        self.check_line([(0, 0), (1, 1), (2, 2)], "X")
        self.check_line([(0, 0), (1, 1), (2, 2)], "O")
        self.check_line([(2, 0), (1, 1), (0, 2)], "X")
        self.check_line([(2, 0), (1, 1), (0, 2)], "O")

        if self.winner == "":
            if len(self.available_positions()) == 0:
                self.winner = "XO"


    def print_hint(self):
        "print hint"
        for v in range(3):
            for h in range(3):
                print(f" {v}{h} ", end="")
            print()


    def print_fld(self):
        "print fld"
        for v in self.board_fld:
            for h in v:
                print(f" {h} ", end="")
            print()


    def available_positions(self):
        "available positions"
        move = []
        for v in range(3):
            for h in range(3):
                if self.board_fld[v][h] == ".":
                    move += [str(v) + str(h)]
        return move

    def play(self):
        "play"
        while self.winner == "":
            self.print_fld()

            move = self.available_positions()

            number = input(f"{move} X: ")

            if number not in move:
                print("неверный ход")
                self.print_hint()
                print()
                continue

            self.board_fld[int(number[0])][int(number[1])] = "X"

            self.is_end_game()

            if self.winner == "":
                move = self.available_positions()

                move0 = move[random.randint(0, len(move) - 1)]

                self.board_fld[int(move0[0])][int(move0[1])] = "O"

                self.is_end_game()

if __name__=="__main__":
    pass
