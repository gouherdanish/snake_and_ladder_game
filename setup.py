from entities.board_dimension import BoardDimension
from entities.entity_type import EntityType
from constants import Constants
from utils import Utils

class BoardSetup:
    def __init__(self) -> None:
        pass

    def choose_board_size(self):
        return BoardDimension(10,10)
    
    def set_snake_positions(self):
        return Utils.load_entity(Constants.SNAKES_FILEPATH,EntityType.SNAKE)
    
    def set_ladder_positions(self):
        return Utils.load_entity(Constants.LADDERS_FILEPATH,EntityType.LADDER)