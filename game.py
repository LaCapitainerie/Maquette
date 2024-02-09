import pygame
import sys
import glob
from bomb import Bomb, Explosion
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
with open(maps[0], "r") as fichier:

    # On lit chaque caractère du fichier
    for l in fichier.read():
        if l == "\n":
            LINE += 1
        elif l != ',':
            terrain_size += 1
            terrain_grid.append(int(l))


# On divise le nombre de case par les lignes pour avoir le nombre de colonne
COL:int = terrain_size // LINE
print(f"Dimension : {COL} / {LINE}")

# On genère les différentes layers
item_grid:list[list] = [0 for _ in range(COL * LINE)]
bomb_grid:list[Bomb] = []


# Make a list of all players
player_list:list[Player] = []

# Création du joueur
joueur:Player = Player(1, 1, "Hugo")
player_list.append(joueur)

# === TEXTURE INITIALISATION ===

player_texture_path:str = "./assets/"
terrain_texture_path:str = "./assets/tiles/"
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

speed = pygame.image.load(f"{bombe_texture_path}speed.png")
onemorebomb = pygame.image.load(f"{bombe_texture_path}onemorebomb.png")

speed = pygame.transform.scale(speed, (int(X_SIZE), int(Y_SIZE)))
onemorebomb = pygame.transform.scale(onemorebomb, (int(X_SIZE), int(Y_SIZE)))

# ==============================



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


            # Une fois que le joueur s'est deplacé
            index = (joueur.y+1) * COL + joueur.x
            
            # Si le joueur est sur un item
            item_cell = item_grid[index]
            match item_cell:
                case 1:
                    joueur.bombe_max += 1
                    item_grid[index] = 0

                case 2:
                    joueur.bombe_speed += 1
                    item_grid[index] = 0
                    

            if event.key == pygame.K_SPACE and terrain_grid[index] != 4:

                # Si le joueur à encore des bombes à poser
                if joueur.bombe_max > joueur.bombe_posee:
                    bomb_grid.append(Bomb(joueur.x, joueur.y+1, joueur.range, terrain_grid[index], joueur, joueur.bombe_speed))
                    joueur.bombe_posee += 1
                    terrain_grid[index] = 4
                
                



    # Affichage de la grille terrain
    for i in range(LINE):
        for j in range(COL):
            index:int = i * COL + j
            cell:int = terrain_grid[index]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))

    BOMB_TIMER:int = 60 #ticks per frame
    EXPLO_TIMER:int = 5 #ticks

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
            terrain_grid[Bombe.x + Bombe.y * COL] = Bombe.cell_from

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
    fenetre.blit(player_image, (joueur.x * X_SIZE, joueur.y * Y_SIZE))


    pygame.display.flip()
    clock.tick(60)
