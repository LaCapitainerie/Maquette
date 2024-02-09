import pygame
import sys
import glob
from bomb import Bomb, Explosion
from player import Player
from gameconfig import *

pygame.init()


# Get all maps from the maps folder ending with .map
maps:list[str] = [f for f in glob.glob("./maps/*.map")]

# On lit le terrain dans le fichier terrain
terrain_size:int = 0
terrain_grid:list[list[int]] = []

with open(maps[1], "r") as fichier:
    terrain_grid = [list(map(int, line.rstrip(',\n').split(','))) for line in fichier.readlines()]

# Size of the terrain
LINE:int = len(terrain_grid)
COL:int = len(terrain_grid[0])


print(f"Dimension : {COL} / {LINE}")

# On genère les différentes layers
item_grid:list[list] = [[0 for _ in range(COL)] for _ in range(LINE)]
bomb_grid:list[Bomb] = []


# Make a list of all players
player_list:list[Player] = []

# Création du joueur
joueur:Player = Player(1, 1, "Hugo")
player_list.append(joueur)

# Setting up textures lists
terrain_list:list[pygame.Surface] = [wall, grass, shadow, brick, air]
bombe_sprite:list[pygame.Surface] = [bombe_0, bombe_1, bombe_2]
explo_sprite:list[pygame.Surface] = [explosion_0, explosion_1, explosion_2, explosion_3, explosion_4, explosion_5]


player_image:pygame.Surface = player_down # On met le sprite par defaut vers le bas

fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()

while True:
    fenetre.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des controles utilisateurs
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and joueur.x > 0:
                if 3 != terrain_grid[joueur.y][joueur.x - 1] != 0 and terrain_grid[joueur.y][joueur.x - 1] != 4:
                    joueur.x -= 1
                player_image = player_left
            elif event.key == pygame.K_RIGHT and joueur.x < COL - 1:
                if 3 != terrain_grid[joueur.y][joueur.x + 1] != 0 and terrain_grid[joueur.y][joueur.x + 1] != 4:
                    joueur.x += 1
                player_image = player_right
            elif event.key == pygame.K_UP and (joueur.y+1) > 0:
                if 3 != terrain_grid[joueur.y - 1][joueur.x] != 0 and terrain_grid[joueur.y - 1][joueur.x] != 4:
                    joueur.y -= 1
                player_image = player_up
            elif event.key == pygame.K_DOWN and (joueur.y+1) < LINE - 1:
                if 3 != terrain_grid[joueur.y + 1][joueur.x] != 0 and terrain_grid[joueur.y + 1][joueur.x] != 4:
                    joueur.y += 1
                player_image = player_down

            
            # Si le joueur est sur un item
            item_cell = item_grid[joueur.y][joueur.x]
            match item_cell:
                case 1:
                    joueur.bombe_max += 1
                    item_grid[joueur.y][joueur.x] = 0

                case 2:
                    joueur.bombe_speed += 1
                    item_grid[joueur.y][joueur.x] = 0
                    

            if event.key == pygame.K_SPACE and terrain_grid[joueur.y][joueur.x] != 4:

                # Si le joueur à encore des bombes à poser
                if joueur.bombe_max > joueur.bombe_posee:
                    bomb_grid.append(Bomb(joueur.x, joueur.y, joueur.range, terrain_grid[joueur.y][joueur.x], joueur, joueur.bombe_speed))
                    joueur.bombe_posee += 1
                    terrain_grid[joueur.y][joueur.x] = 4
                
                


    # Affichage de la grille terrain
    for i in range(LINE):
        for j in range(COL):
            cell:int = terrain_grid[i][j]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))

    # Pour chaque bombe posée
    for Bombe in bomb_grid:

        # On tick la bombe selon son tick rate (cf. power up)
        Bombe.tick += Bombe.tick_rate

        #print(Bombe.tick)
        # Si la bombe explose
        if Bombe.tick == BOMB_TIMER*3:

            # On actualise la capacité du joueur
            Bombe.origin.bombe_posee -= 1

            # On replace le terrain d'origine
            terrain_grid[Bombe.y][Bombe.x] = Bombe.cell_from

            # On regarde dans les 4 directions via la fonction Explosion
            Explosion(Map=terrain_grid, Line=LINE, Col=COL, Bombe=Bombe, Players=player_list, Item_map=item_grid)

            





        elif Bombe.tick >= (BOMB_TIMER*3 + EXPLO_TIMER*6):
            
            """
            On doit attendre la fin de l'anim de l'explosion
            à ajouter
            """

            # Et enfin on retire la bombe
            bomb_grid.remove(Bombe)
            del Bombe

        else:
            
            # Sinon on affiche la texture de la bombe
            # Si elle n'a pas encore explosée
            if Bombe.tick < BOMB_TIMER*3:
                # Le sprite de la bombe en cours d'explosion
                fenetre.blit(bombe_sprite[Bombe.tick//BOMB_TIMER], (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))
            else:
                # Sinon le sprite de l'explosion
                if Bombe.tick % EXPLO_TIMER == 0:
                    fenetre.blit(grass, (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))
                fenetre.blit(explo_sprite[(Bombe.tick - BOMB_TIMER*3)//EXPLO_TIMER], (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))


    for i in range(len(item_grid)):
        match item_grid[i]:
            case 1:
                fenetre.blit(onemorebomb, (i%COL * X_SIZE, i//COL * Y_SIZE))
                
            case 2:
                fenetre.blit(speed, (i%COL * X_SIZE, i//COL * Y_SIZE))
                



    # Et enfin on affiche le joueur
    fenetre.blit(player_image, (joueur.x * X_SIZE,(joueur.y - 1) * Y_SIZE))


    pygame.display.flip()
    clock.tick(60)
