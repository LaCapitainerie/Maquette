class Player():

    def __init__(self, x:int, y:int, name:str) -> None:
        self.name = name
        self.x = x
        self.y = y

        # Nombre de bombe
        self.bombe_max = 1
        self.bombe_posee = 0

        # Detail des bombes
        self.range = 2
        pass