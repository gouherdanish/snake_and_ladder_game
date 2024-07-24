class Game:
    def __init__(self,board,dice) -> None:
        self.board = board
        self.dice = dice
        self.players = []
        self.numOf_active_players = 0

    def add_player(self,player):
        self.players.append(player)
        player.activate()

    def is_over(self):
        return self.numOf_active_players < 2
    
