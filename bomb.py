from player import Player

class Bomb():

    def __init__(self, x:int, y:int, range:int, cell_from:int, origin:Player):
        # Position of the Bomb
        self.x = x
        self.y = y

        # Previous cell the bomb was on
        self.cell_from = cell_from

        # Ticking of the Bomb
        self.tick = 0

        # Size of the explosion
        self.range = range

        # Set the Name of the placer
        self.origin = origin
        pass