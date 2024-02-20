import pygame
import sys
import glob
from gameconfig import *

pygame.init()


"""

Important ajouter un retour à la ligne à la fin du fichier

"""





# Get all maps from the maps folder ending with .map
maps:list[str] = [f for f in glob.glob("./maps/*.map")]


# On lit le terrain dans le fichier terrain
terrain_size:int = 0
terrain_grid:list[list[int]] = []

with open(maps[0], "r") as fichier:
    terrain_grid = [list(map(int, line.rstrip(',\n').split(','))) for line in fichier.readlines()]

# Size of the terrain
LINE:int = len(terrain_grid)
COL:int = len(terrain_grid[0])




# Init la fenêtre
fenetre = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()

# Init des variables/constantes pour la modification de terrain
terrain_list:list[pygame.Surface] = [wall, grass, shadow, brick, air]
cursor:int = 0

while True:

    fenetre.fill((0, 0, 0))
    x, y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion des controles utilisateurs
        elif event.type == pygame.KEYDOWN:
            # Cette partie là s'occupe du changement de case à placer via les touches
            if event.key == pygame.K_1:
                cursor = 0
            elif event.key == pygame.K_2:
                cursor = 1
            elif event.key == pygame.K_3:
                cursor = 2
            elif event.key == pygame.K_4:
                cursor = 3
            elif event.key == pygame.K_5:
                cursor = 4


            elif event.key == pygame.K_s:
                print("saving..")

                # On crée une liste de sauvegarde des caractères
                save:str = ""
                for i in range(LINE):
                    for j in range(COL):
                        save += str(terrain_grid[i][j])
                        save += ','
                    save += '\n'
                        

                # Solution temporaire pour ne pas utiliser join
                save = save[:-2]

                # Création et Ouverture du fichier de save
                with open("./maps/save.map", "w+") as file:
                    # Ecriture dans le fichier de la map
                    file.write(save)
                print("saved!")
                


        elif event.type == pygame.MOUSEBUTTONDOWN:
            terrain_grid[(y//Y_SIZE)][(x//X_SIZE)] = cursor
    
    # Affichage de la grille terrain
    for i in range(LINE):
        for j in range(COL):

            # On affiche la case qui correspond au bon endroit
            cell:int = terrain_grid[i][j]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))
    
    # Affichage de la tile sur la souris
    fenetre.blit(terrain_list[cursor], (x - (X_SIZE>>1), y - (Y_SIZE>>1)))

    pygame.display.flip()
    clock.tick(60)