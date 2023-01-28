from board import Board
from gui import BoardGui

class Game():

    def __init__(self):
        self.board = Board(row_size=4, col_size=4)
        self.boardGui = BoardGui(self.board)

    def start(self):
        self.boardGui.loop()

if __name__ == "__main__":
    g = Game()
    g.start()