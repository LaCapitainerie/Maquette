import pygame
import sys
import glob

pygame.init()

# Ratio of the screen
WIDTH = 1600
HEIGHT = 600

# Size of the terrain
LINE = 9

# Parameter of the zoom
ZOOM = 2


# Size of the assets
X_SIZE = 16 * ZOOM
Y_SIZE = 16 * ZOOM

# Get all maps from the maps folder
maps = [f for f in glob.glob("./maps/*.map")]

# On lit le terrain dans le fichier terrain
with open(maps[1], "r") as fichier:
    terrain_grid = [int(nombre) for nombre in fichier.read().split(',')]
COL = len(terrain_grid) // LINE

item_grid:list[list] = [0 for _ in range(COL * LINE)]

pos_joueur = [1, 1]

player_texture_path:str = "./player assets/"
terrain_texture_path:str = "./terrain assets/"
bombe_texture_path:str = "./bombe assets/"

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

terrain_list = [wall, grass, shadow, brick, air]
item_list = [bombe_0, bombe_1, bombe_2]


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
            index = (pos_joueur[1]+1) * COL + pos_joueur[0]
            print(index, item_grid, item_grid[index])
            if event.key == pygame.K_LEFT and pos_joueur[0] > 0:
                if 3 != terrain_grid[index - 1] != 0 and terrain_grid[index - 1] != 4:
                    pos_joueur[0] -= 1
                player_image = player_left
            elif event.key == pygame.K_RIGHT and pos_joueur[0] < COL - 1:
                if 3 != terrain_grid[index + 1] != 0 and terrain_grid[index + 1] != 4:
                    pos_joueur[0] += 1
                player_image = player_right
            elif event.key == pygame.K_UP and (pos_joueur[1]+1) > 0:
                if 3 != terrain_grid[index - COL] != 0 and terrain_grid[index - COL] != 4:
                    pos_joueur[1] -= 1
                player_image = player_up
            elif event.key == pygame.K_DOWN and (pos_joueur[1]+1) < LINE - 1:
                if 3 != terrain_grid[index + COL] != 0 and terrain_grid[index + COL] != 4:
                    pos_joueur[1] += 1
                player_image = player_down

            elif event.key == pygame.K_SPACE and item_grid[index] == 0:
                item_grid[index] = 4
                terrain_grid[index] = 4
                
                



    # Affichage de la grille terrain
    for i in range(LINE):
        for j in range(COL):
            index = i * COL + j
            cell = terrain_grid[index]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))

            # Si on affiche un terrain disponible
            # Affichage de la grille item
            objet = item_grid[index]
            if objet > 3:

                # Incrémentation du compteur de la bombe
                item_grid[index] += 1
                
                BOMB_TIMER = 60 #ticks

                # Si la bombe est arrivée à la fin du décompte
                if item_grid[index] == BOMB_TIMER* 3:
                    # On retire la bombe
                    item_grid[index] = 0
                    terrain_grid[index] = 1

                    # Puis on execute les actions de la bombe

                else:
                    # Affichage des bombes
                    fenetre.blit(item_list[item_grid[index]//BOMB_TIMER], (j * X_SIZE, i * Y_SIZE))




    fenetre.blit(player_image, (pos_joueur[0] * X_SIZE, pos_joueur[1] * Y_SIZE))


    pygame.display.flip()
    clock.tick(60)
