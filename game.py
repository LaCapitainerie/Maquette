import pygame
import sys
import glob
from bomb import Bomb
from player import Player

pygame.init()

# Ratio of the screen
WIDTH = 800
HEIGHT = 600

# Size of the terrain
LINE = 9
COL = None

# Parameter of the zoom
ZOOM = 2


# Size of the assets
X_SIZE = 16 * ZOOM
Y_SIZE = 16 * ZOOM

# Get all maps from the maps folder ending with .map
maps = [f for f in glob.glob("./maps/*.map")]

# On lit le terrain dans le fichier terrain
with open(maps[1], "r") as fichier:
    terrain_grid = [int(nombre) for nombre in fichier.read().split(',')]
COL = len(terrain_grid) // LINE

item_grid:list[list] = [0 for _ in range(COL * LINE)]
bomb_grid:list[Bomb] = []

# Création du joueur
joueur = Player(1, 1, "Hugo")

# === TEXTURE INITIALISATION ===

player_texture_path:str = "./assets/"
terrain_texture_path:str = "./assets/"
bombe_texture_path:str = "./assets/"

player_up = pygame.image.load(f"{player_texture_path}player_up.png")
player_down = pygame.image.load(f"{player_texture_path}player_down.png")
player_left = pygame.image.load(f"{player_texture_path}player_left.png")
player_right = pygame.image.load(f"{player_texture_path}player_right.png")

player_up = pygame.transform.scale(player_up, (X_SIZE, 32*ZOOM))
player_down = pygame.transform.scale(player_down, (X_SIZE, 32*ZOOM))
player_left = pygame.transform.scale(player_left, (X_SIZE, 32*ZOOM))
player_right = pygame.transform.scale(player_right, (X_SIZE, 32*ZOOM))

wall = pygame.image.load(f"{terrain_texture_path}wall.jpg")
grass = pygame.image.load(f"{terrain_texture_path}grass.jpg")
shadow = pygame.image.load(f"{terrain_texture_path}shadow.jpg")
brick = pygame.image.load(f"{terrain_texture_path}brick.jpg")
air = pygame.image.load(f"{terrain_texture_path}grass.jpg")

wall = pygame.transform.scale(wall, (int(X_SIZE), int(Y_SIZE)))
grass = pygame.transform.scale(grass, (int(X_SIZE), int(Y_SIZE)))
shadow = pygame.transform.scale(shadow, (int(X_SIZE), int(Y_SIZE)))
brick = pygame.transform.scale(brick, (int(X_SIZE), int(Y_SIZE)))
air = pygame.transform.scale(air, (int(X_SIZE), int(Y_SIZE)))

bombe_0 = pygame.image.load(f"{bombe_texture_path}bombe_0.png")
bombe_1 = pygame.image.load(f"{bombe_texture_path}bombe_1.png")
bombe_2 = pygame.image.load(f"{bombe_texture_path}bombe_2.png")

bombe_0 = pygame.transform.scale(bombe_0, (int(X_SIZE), int(Y_SIZE)))
bombe_1 = pygame.transform.scale(bombe_1, (int(X_SIZE), int(Y_SIZE)))
bombe_2 = pygame.transform.scale(bombe_2, (int(X_SIZE), int(Y_SIZE)))

# ==============================



terrain_list = [wall, grass, shadow, brick, air]
bombe_sprite = [bombe_0, bombe_1, bombe_2]




player_image = player_down

fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
        elif event.type == pygame.KEYDOWN:
            index = (joueur.y+1) * COL + joueur.x
            if event.key == pygame.K_LEFT and joueur.x > 0:
                if 3 != terrain_grid[index - 1] != 0 and terrain_grid[index - 1] != 4:
                    joueur.x -= 1
                player_image = player_left
            elif event.key == pygame.K_RIGHT and joueur.x < COL - 1:
                if 3 != terrain_grid[index + 1] != 0 and terrain_grid[index + 1] != 4:
                    joueur.x += 1
                player_image = player_right
            elif event.key == pygame.K_UP and (joueur.y+1) > 0:
                if 3 != terrain_grid[index - COL] != 0 and terrain_grid[index - COL] != 4:
                    joueur.y -= 1
                player_image = player_up
            elif event.key == pygame.K_DOWN and (joueur.y+1) < LINE - 1:
                if 3 != terrain_grid[index + COL] != 0 and terrain_grid[index + COL] != 4:
                    joueur.y += 1
                player_image = player_down

            elif event.key == pygame.K_SPACE and terrain_grid[index] != 4:

                # Si le joueur à encore des bombes à poser
                if joueur.bombe_max > joueur.bombe_posee:
                    bomb_grid.append(Bomb(joueur.x, joueur.y+1, joueur.range, terrain_grid[index], joueur))
                    joueur.bombe_posee += 1
                    terrain_grid[index] = 4
                
                



    # Affichage de la grille terrain
    for i in range(LINE):
        for j in range(COL):
            index = i * COL + j
            cell = terrain_grid[index]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))

    BOMB_TIMER = 60 #ticks per frame

    # Pour chaque bombe posée
    for Bombe in bomb_grid:
        Bombe.tick += 1

        # Si la bombe explose
        if Bombe.tick == 180:
            # On actualise la capacité du joueur
            Bombe.origin.bombe_posee -= 1
            # On replace le terrain d'origine
            terrain_grid[Bombe.x + Bombe.y * COL] = Bombe.cell_from

            for i in range(Bombe.x - Bombe.range, Bombe.x + Bombe.range + 1):
                idx = i + Bombe.y * COL
                print(idx, terrain_grid[idx])
                # Si la bombe explose sur un mur
                if terrain_grid[idx] == 3:
                    # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                    terrain_grid[idx] = 1 if terrain_grid[idx - COL] != 0 and terrain_grid[idx - COL] != 3 else 2

                    # Si la case en dessous est une ombre changer le sprite
                    terrain_grid[idx + COL] = 1

            for i in range(Bombe.y - Bombe.range, Bombe.y + Bombe.range + 1):
                idx = Bombe.x + i * COL

                # Si la bombe explose sur un mur
                if terrain_grid[idx] == 3:
                    # On regarde la case superieur pour savoir si remplacer par une ombre ou un plain
                    terrain_grid[idx] = 1 if terrain_grid[idx - COL] != 0 and terrain_grid[idx - COL] != 3 else 2

                    # Si la case en dessous est une ombre changer le sprite
                    terrain_grid[idx + COL] = 1


            # Et enfin on retire la bombe
            bomb_grid.remove(Bombe)
            del Bombe
        
        # Sinon on affiche la texture de la bombe
        else:
            fenetre.blit(bombe_sprite[Bombe.tick//BOMB_TIMER], (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))


    fenetre.blit(player_image, (joueur.x * X_SIZE, joueur.y * Y_SIZE))


    pygame.display.flip()
    clock.tick(60)
