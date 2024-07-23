from setup import BoardSetup
from entities.board import Board
from entities.dice import Dice
from entities.game import Game

if __name__ == '__main__':
    setup       = BoardSetup()
    board_size  = setup.choose_board_size()
    snake_pos   = setup.set_snake_positions()
    ladder_pos  = setup.set_ladder_positions()

    board       = Board(board_size,snake_pos,ladder_pos)
    dice        = Dice()
    game        = Game(board,dice)