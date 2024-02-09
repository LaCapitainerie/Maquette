import pygame;

# Ratio of the screen
WIDTH:int = 800
HEIGHT:int = 600

# Parameter of the zoom
ZOOM:int = 2

# Size of the assets
X_SIZE:int = 16 * ZOOM
Y_SIZE:int = 16 * ZOOM

# Bomb timer
BOMB_TIMER:int = 60 #ticks per frame
EXPLO_TIMER:int = 5 #ticks


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