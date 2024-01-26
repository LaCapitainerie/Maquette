import pygame
import sys
import glob
from bomb import Bomb
from player import Player

pygame.init()

# Ratio of the screen
WIDTH:int = 800
HEIGHT:int = 600

# Size of the terrain
LINE:int = 1
COL:int = 0

# Parameter of the zoom
ZOOM:int = 2


# Size of the assets
X_SIZE:int = 16 * ZOOM
Y_SIZE:int = 16 * ZOOM

# Get all maps from the maps folder ending with .map
maps:list[str] = [f for f in glob.glob("./maps/*.map")]

# On lit le terrain dans le fichier terrain
terrain_size:int = 0
terrain_grid:list[int] = []
with open(maps[1], "r") as fichier:

    # On lit chaque caractère du fichier
    for l in fichier.read():
        if l == "\n":
            LINE += 1
        elif l != ',':
            terrain_size += 1
            terrain_grid.append(int(l))


# On divise le nombre de case par les lignes pour avoir le nombre de colonne
COL:int = terrain_size // LINE

# On genère les différentes layers
item_grid:list[list] = [0 for _ in range(COL * LINE)]
bomb_grid:list[Bomb] = []

# Création du joueur
joueur:Player = Player(1, 1, "Hugo")

# === TEXTURE INITIALISATION ===

player_texture_path:str = "./assets/"
terrain_texture_path:str = "./assets/"
bombe_texture_path:str = "./assets/"
explosion_texture_path:str = "./assets/"

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

explosion_0 = pygame.image.load(f"{explosion_texture_path}explosion_0.png")
explosion_1 = pygame.image.load(f"{explosion_texture_path}explosion_1.png")
explosion_2 = pygame.image.load(f"{explosion_texture_path}explosion_2.png")
explosion_3 = pygame.image.load(f"{explosion_texture_path}explosion_3.png")
explosion_4 = pygame.image.load(f"{explosion_texture_path}explosion_4.png")
explosion_5 = pygame.image.load(f"{explosion_texture_path}explosion_5.png")

explosion_0 = pygame.transform.scale(explosion_0, (int(X_SIZE), int(Y_SIZE)))
explosion_1 = pygame.transform.scale(explosion_1, (int(X_SIZE), int(Y_SIZE)))
explosion_2 = pygame.transform.scale(explosion_2, (int(X_SIZE), int(Y_SIZE)))
explosion_3 = pygame.transform.scale(explosion_3, (int(X_SIZE), int(Y_SIZE)))
explosion_4 = pygame.transform.scale(explosion_4, (int(X_SIZE), int(Y_SIZE)))
explosion_5 = pygame.transform.scale(explosion_5, (int(X_SIZE), int(Y_SIZE)))

# ==============================



terrain_list:list[pygame.Surface] = [wall, grass, shadow, brick, air]
bombe_sprite:list[pygame.Surface] = [bombe_0, bombe_1, bombe_2]
explo_sprite:list[pygame.Surface] = [explosion_0, explosion_1, explosion_2, explosion_3, explosion_4, explosion_5]




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
            index:int = i * COL + j
            cell:int = terrain_grid[index]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))

    BOMB_TIMER:int = 60 #ticks per frame
    EXPLO_TIMER:int = 20 #ticks

    # Pour chaque bombe posée
    for Bombe in bomb_grid:
        Bombe.tick += 1

        print(Bombe.tick)
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

        elif Bombe.tick == 300:
            
            """
            On doit attendre la fin de l'anim de l'explosion
            à ajouter
            """

            # Et enfin on retire la bombe
            bomb_grid.remove(Bombe)
            del Bombe

        else:
            
            # Sinon on affiche la texture de la bombe
            if Bombe.tick < 180:
                fenetre.blit(bombe_sprite[Bombe.tick//BOMB_TIMER], (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))
            else:
                if Bombe.tick % EXPLO_TIMER == 0:
                    fenetre.blit(grass, (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))
                fenetre.blit(explo_sprite[(Bombe.tick - 180)//EXPLO_TIMER], (Bombe.x * X_SIZE, Bombe.y * Y_SIZE))


    fenetre.blit(player_image, (joueur.x * X_SIZE, joueur.y * Y_SIZE))


    pygame.display.flip()
    clock.tick(60)
