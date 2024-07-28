class Game:
    def __init__(self,board,dice) -> None:
        self.board = board
        self.dice = dice
        self.players = []
        self.numOf_active_players = 0

    def add_player(self,player):
        self.players.append(player)
        player.activate()
        self.numOf_active_players += 1

    def is_over(self):
        return self.numOf_active_players < 2
    
    def start(self):
        print('Game Started !')
        rank = 0
        while not self.is_over():
            for player in self.players:
                if player.is_playing() and not self.is_over():        
                    try:
                        pos = player.get_pos()
                        roll = self.dice.roll()
                        print(f"{player.get_name()}'s turn : Current pos - {pos} Dice Roll - {roll}")
                        next_pos = self.board.get_next_pos(pos,roll)
                        player.set_pos(next_pos)
                        if next_pos == self.board.get_total_cells():
                            print(f'{player.get_name()} Won')
                            player.deactivate()
                            rank += 1
                            player.set_ranking(rank)
                            self.numOf_active_players -= 1
                    except Exception as e:
                        print(e)
    
    def finish(self):
        max_rank = 0
        for player in self.players:
            player_rank = player.get_ranking()
            max_rank = max(player_rank,max_rank)
            if player_rank == 0:
                player.set_ranking(max_rank+1)

    def get_rankings(self):
        return {player.name:player.ranking for player in self.players}


