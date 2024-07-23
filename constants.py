import os

class Constants:
    CUR_DIR = os.path.dirname(__file__)
    DATA_DIR = os.path.join(CUR_DIR,'resources')
    SNAKES_FILEPATH = os.path.join(DATA_DIR,'snakes.txt')
    LADDERS_FILEPATH = os.path.join(DATA_DIR,'ladders.txt')