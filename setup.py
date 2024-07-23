from entities.board_dimension import BoardDimension
from constants import Constants
from utils import Utils

class BoardSetup:
    def __init__(self) -> None:
        pass

    def choose_board_size(self):
        return BoardDimension(10,10)
    
    def set_snake_positions(self):
        return Utils.load_txt(Constants.SNAKES_FILEPATH)
    
    def set_ladder_positions(self):
        return Utils.load_txt(Constants.LADDERS_FILEPATH)