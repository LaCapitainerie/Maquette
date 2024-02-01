from player import Player
from random import randint

class Bomb():

    def __init__(self, x:int, y:int, range:int, cell_from:int, origin:Player, speed:int):
        # Position of the Bomb
        self.x = x
        self.y = y

        # Previous cell the bomb was on
        self.cell_from = cell_from

        # Ticking of the Bomb
        self.tick = 0
        self.tick_rate = speed

        # Size of the explosion
        self.range = range

        # Set the Name of the placer
        self.origin = origin
        pass


def Explosion(Map:list[int], Col:int, Bombe:Bomb, Players:list[Player], Item_map:list[int]):

    # Explosion vers la droite
    for i in range(1, Bombe.range + 1):
        idx = Bombe.x + i + Bombe.y * Col
        cel = Map[idx]
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x + i and joueur.y + 1 == Bombe.y:
                    print(f"Joueur {joueur.name} est mort.")
                    


            # Si la bombe explose sur un mur
            if Map[idx] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[idx] = make_item()



                # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                Map[idx] = 1 if Map[idx - Col] != 0 and Map[idx - Col] != 3 else 2

                # Si la case en dessous est une ombre changer le sprite
                Map[idx + Col] = 1
        pass

    # Explosion vers la gauche
    for i in range(1, Bombe.range + 1):
        idx = Bombe.x - i + Bombe.y * Col
        cel = Map[idx]
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x - i and joueur.y + 1== Bombe.y:
                    print(f"Joueur {joueur.name} est mort.")


            # Si la bombe explose sur un mur
            if Map[idx] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[idx] = make_item()


                # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                Map[idx] = 1 if Map[idx - Col] != 0 and Map[idx - Col] != 3 else 2

                # Si la case en dessous est une ombre changer le sprite
                Map[idx + Col] = 1
        pass

    # Explosion vers le bas
    for i in range(1, Bombe.range + 1):
        idx = Bombe.x + (Bombe.y + i) * Col
        cel = Map[idx]
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x and joueur.y + 1 == Bombe.y + i:
                    print(f"Joueur {joueur.name} est mort.")


            # Si la bombe explose sur un mur
            if Map[idx] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[idx] = make_item()


                # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                Map[idx] = 1 if Map[idx - Col] != 0 and Map[idx - Col] != 3 else 2

                # Si la case en dessous est une ombre changer le sprite
                Map[idx + Col] = 1
        pass

    # Explosion vers le haut
    for i in range(1, Bombe.range + 1):
        idx = Bombe.x + (Bombe.y - i) * Col
        cel = Map[idx]
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x and joueur.y + 1 == Bombe.y - i:
                    print(f"Joueur {joueur.name} est mort.")


            # Si la bombe explose sur un mur
            if Map[idx] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[idx] = make_item()


                # On ne regarde pas car la case du haut à forcément explosée
                Map[idx] = 1

                # Si la case en dessous est une ombre changer le sprite
                Map[idx + Col] = 1
        pass
    pass


def make_item() -> int:
    r = randint(1, 5)
    print(r)

    result = 0
    # Doit-on dropper un item
    match r:
        case 4:
            result = 2
        
        case 5:
            result = 1

    # On retourne le resultat
    return result
    pass