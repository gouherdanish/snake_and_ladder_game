class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.is_playing_flag = False
        self.current_pos = 0

    def move(self,pos):
        self.current_pos = pos

    @property
    def is_playing(self):
        return self.is_playing_flag

    def activate(self):
        self.is_playing = True

    def deactivate(self):
        self.is_playing = False