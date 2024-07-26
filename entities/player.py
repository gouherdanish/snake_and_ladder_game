class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.is_playing_flag = False
        self.current_pos = 0
        self.ranking = 0

    def __str__(self) -> str:
        return f'Player(name={self.name},rank={self.ranking})'
    
    def __repr__(self) -> str:
        return str(self)

    def get_name(self):
        return self.name

    def get_pos(self):
        return self.current_pos

    def set_pos(self,pos):
        print(f'{self.name} moved from {self.current_pos} to {pos}')
        self.current_pos = pos

    def is_playing(self):
        return self.is_playing_flag

    def activate(self):
        self.is_playing_flag = True

    def deactivate(self):
        self.is_playing_flag = False

    def set_ranking(self,rank):
        self.ranking = rank

    def get_ranking(self):
        return self.ranking