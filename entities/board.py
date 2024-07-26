

class Board:
    def __init__(self,board_size,snakes,ladders) -> None:
        self.board_size = board_size
        self.snakes = snakes
        self.ladders = ladders
        self.total_cells = self.board_size.rows * self.board_size.cols
        self._set_position_mapping()

    def _set_position_mapping(self):
        self.pos_map = {i:i for i in range(1,self.total_cells+1)}
        for snake in self.snakes:
            self.pos_map[snake.get_start()] = snake.get_end()
        for ladder in self.ladders:
            self.pos_map[ladder.get_start()] = ladder.get_end()

    def get_total_cells(self):
        return self.total_cells
    
    def get_next_pos(self,pos,roll):
        if pos + roll > self.total_cells:
            raise Exception(f"Invalid Move: Can't move to pos {pos + roll}")
        return self.pos_map[pos+roll]

