class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.is_playing = False
        self.current_pos = 0

    def move(self,pos):
        self.current_pos = pos

    def activate(self):
        self.is_playing = True

    def deactivate(self):
        self.is_playing = False