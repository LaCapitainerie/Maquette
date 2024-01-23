import pygame
import sys

pygame.init()

largeur_fenetre = 800
hauteur_fenetre = 600

nb_colonnes = 11
nb_lignes = 13
ZOOM = 2
X_SIZE = 16 * ZOOM
Y_SIZE = 16 * ZOOM

with open("couleurs.txt", "r") as fichier:
    liste_nombres = [int(nombre) for nombre in fichier.read().split(',')]

pos_joueur = [0, 0]

player_texture_path:str = "./player/"
terrain_texture_path:str = "./terrain/"

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

wall = pygame.transform.scale(wall, (int(X_SIZE), int(Y_SIZE)))
grass = pygame.transform.scale(grass, (int(X_SIZE), int(Y_SIZE)))
shadow = pygame.transform.scale(shadow, (int(X_SIZE), int(Y_SIZE)))
brick = pygame.transform.scale(brick, (int(X_SIZE), int(Y_SIZE)))

terrain_list = [wall, grass, shadow, brick]


player_image = player_down

fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Grille de pixels")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and pos_joueur[0] > 0:
                pos_joueur[0] -= 1
                player_image = player_left
            elif event.key == pygame.K_RIGHT and pos_joueur[0] < nb_colonnes - 1:
                pos_joueur[0] += 1
                player_image = player_right
            elif event.key == pygame.K_UP and pos_joueur[1] > 0:
                pos_joueur[1] -= 1
                player_image = player_up
            elif event.key == pygame.K_DOWN and pos_joueur[1] < nb_lignes - 1:
                pos_joueur[1] += 1
                player_image = player_down


    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            cell = liste_nombres[i * nb_colonnes + j]
            fenetre.blit(terrain_list[cell], (j * X_SIZE, i * Y_SIZE))



    fenetre.blit(player_image, (pos_joueur[0] * X_SIZE, pos_joueur[1] * Y_SIZE))


    pygame.display.flip()
