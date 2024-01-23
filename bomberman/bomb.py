import pygame
import random

pygame.init()

# Constantes
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
PLAYER_SIZE = 40
BOMB_SIZE = 40
PLAYER_SPEED = 5
BOMB_TIMER = 120
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        new_rect = self.rect.copy()

        if keys[pygame.K_LEFT]:
            new_rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            new_rect.x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            new_rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            new_rect.y += PLAYER_SPEED

        for wall in walls:
            if new_rect.colliderect(wall.rect):
                return

        if 0 <= new_rect.left <= WIDTH - PLAYER_SIZE and 0 <= new_rect.top <= HEIGHT - PLAYER_SIZE:
            self.rect = new_rect

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((BOMB_SIZE, BOMB_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.timer = BOMB_TIMER

    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.kill()

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

game_grid = [[None for _ in range(WIDTH // TILE_SIZE)] for _ in range(HEIGHT // TILE_SIZE)]

def generate_walls():
    walls = pygame.sprite.Group()
    for i in range(WIDTH // TILE_SIZE):
        for j in range(HEIGHT // TILE_SIZE):
            if random.random() < 0.2:
                wall = Wall(i * TILE_SIZE, j * TILE_SIZE)
                walls.add(wall)
                game_grid[j][i] = wall
    return walls

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maquette bombe")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(WIDTH // 2, HEIGHT // 2)
all_sprites.add(player)

walls = generate_walls()
all_sprites.add(walls)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bomb = Bomb(TILE_SIZE*(player.rect.x//TILE_SIZE), TILE_SIZE*(player.rect.y//TILE_SIZE))
                all_sprites.add(bomb)

    player.update()
    all_sprites.update()

    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
