#!/usr/bin/env python
# -*-coding:utf-8 -*-

import fire

from board import Board

class Game():

    def __init__(self):
        self.board = Board(row_size=4, col_size=4)


    def gui(self):
        from gui import BoardGui
        boardGui = BoardGui(self.board)
        boardGui.loop()


    def cli(self):
        moved = False
        self.board.generate()

        while True:
            if moved:
                self.board.generate()

            moved = False
            print(self.board)
            action = input("action (l, r, u, d): ")

            if action == "l":
                moved = self.board.left()
            if action == "r":
                moved = self.board.right()
            if action == "u":
                moved = self.board.up()
            if action == "d":
                moved = self.board.down()

            print("-"*23)

    def __call__(self):
        self.cli()

if __name__ == "__main__":
    fire.Fire(Game)