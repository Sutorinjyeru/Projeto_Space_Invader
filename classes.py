class Ship():
    def __init__(self, sprite, position_x, position_y, movement):
        self.sprite = sprite
        self.position_x = position_x
        self.position_y = position_y
        self.movement = movement

class Player(Ship):
    def __init__(self, sprite, position_x, position_y, movement):
        super().__init__(sprite, position_x, position_y, movement)
    


class Enemy(Ship):
    def __init__(self, sprite, position_x, position_y, movement):
        super().__init__(sprite, position_x, position_y, movement)