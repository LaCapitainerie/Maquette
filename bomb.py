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


def Explosion(Map:list[list[int]], Line:int, Col:int, Bombe:Bomb, Players:list[Player], Item_map:list[int]):

    # Explosion vers la droite
    for i in range(1, Bombe.range + 1):
        # Si on est hors du terrain on arrete
        if (Bombe.x + i) == Col:
            break
        cel = Map[Bombe.y][Bombe.x + i]
        # Si on tape contre un mur on arrête la deflagration
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x + i and joueur.y + 1 == Bombe.y:
                    print(f"Joueur {joueur.name} est mort.")
                    


            # Si la bombe explose sur un mur
            if Map[Bombe.y][Bombe.x + i] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[Bombe.y][Bombe.x + i] = make_item()



                # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                Map[Bombe.y][Bombe.x + i] = 1 if Map[Bombe.y - 1][Bombe.x + i] != 0 and Map[Bombe.y - 1][Bombe.x + i] != 3 else 2

                # Si la case en dessous est une ombre changer le sprite
                Map[Bombe.y + 1][Bombe.x + i] = 1
        pass

    # Explosion vers la gauche
    for i in range(1, Bombe.range + 1):
        # Si on est hors du terrain on arrete
        if (Bombe.x - i) == Col:
            break
        cel = Map[Bombe.y][Bombe.x - i]
        # Si on tape contre un mur on arrête la deflagration
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x - i and joueur.y + 1 == Bombe.y:
                    print(f"Joueur {joueur.name} est mort.")
                    


            # Si la bombe explose sur un mur
            if Map[Bombe.y][Bombe.x - i] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[Bombe.y][Bombe.x - i] = make_item()


                # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                Map[Bombe.y][Bombe.x - i] = 1 if Map[Bombe.y][Bombe.x - i] != 0 and Map[Bombe.y][Bombe.x - i] != 3 else 2

                # Si la case en dessous est une ombre changer le sprite
                Map[Bombe.y + 1][Bombe.x - i] = 1
        pass

    # Explosion vers le bas
    for i in range(1, Bombe.range + 1):

        # Si on est hors du terrain on arrete
        if (Bombe.y + i) == Line:
            break

        cel = Map[Bombe.y + i][Bombe.x]
        # Si on tape contre un mur on arrête la deflagration
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x and joueur.y + 1 == Bombe.y + i:
                    print(f"Joueur {joueur.name} est mort.")


            # Si la bombe explose sur un mur
            if Map[Bombe.y + i][Bombe.x] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[Bombe.y + i][Bombe.x] = make_item()

                # Comme la bombe était au dessus il ne peut pas y avoir de bloc qui fait de l'ombre
                Map[Bombe.y + i][Bombe.x] = 1
                
                # Si la case en dessous est une ombre changer le sprite
                Map[Bombe.y + i + 1][Bombe.x] = 1
        pass

    # Explosion vers le Haut
    for i in range(1, Bombe.range + 1):

        # Si on est hors du terrain on arrete
        if (Bombe.y - i) == Line:
            break
        cel = Map[Bombe.y - i][Bombe.x]
        # Si on tape contre un mur on arrête la deflagration
        if cel == 0:
            break
        else:
            # Si la bombe explose sur un joueur :
            for joueur in Players:
                if joueur.x == Bombe.x and joueur.y + 1 == Bombe.y - i:
                    print(f"Joueur {joueur.name} est mort.")


            # Si la bombe explose sur un mur
            if Map[Bombe.y - i][Bombe.x] == 3:

                # On appelle le generateur d'item qui renvoi ou non un item
                Item_map[Bombe.y - i][Bombe.x] = make_item()


                # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                Map[Bombe.y - i][Bombe.x] = 1 if Map[Bombe.y - i - 1][Bombe.x] != 0 and Map[Bombe.y - i - 1][Bombe.x] != 3 else 2


                # Si la case en dessous est une ombre changer le sprite
                Map[Bombe.y - i + 1][Bombe.x] = 1
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