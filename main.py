from board import Board
from game import Game



if __name__ == '__main__':
    board = Board(6,6)
    game = Game(board)
    option = int(raw_input('1. Display Board\n2. Play Game\n'))
    if(option == 1):
        board.display()
    else:
        game.play(0.8,0)