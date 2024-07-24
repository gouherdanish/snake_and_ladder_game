from setup import BoardSetup
from entities.board import Board
from entities.dice import Dice
from entities.game import Game
from entities.player import Player

if __name__ == '__main__':
    setup       = BoardSetup()
    board_size  = setup.choose_board_size()
    snake_pos   = setup.set_snake_positions()
    ladder_pos  = setup.set_ladder_positions()

    board       = Board(board_size,snake_pos,ladder_pos)
    dice        = Dice()
    game        = Game(board,dice)
    
    num_players = input('How many players ?')
    for i in range():
        name = input(f'Player {i+1} name: ')
        player = Player(name)
        game.add_player(player)
    
    game.start()