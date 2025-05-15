import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Dash Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Car dimensions
CAR_WIDTH, CAR_HEIGHT = 40, 70

# Player car setup
player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 20
player_speed = 5

# Enemy car setup
enemy_speed = 5
enemy_timer = 0
enemy_delay = 30  # Frames between new enemy cars
enemies = []

def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, CAR_WIDTH, CAR_HEIGHT))

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(GRAY)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - CAR_WIDTH:
        player_x += player_speed

    # Spawn enemy cars
    enemy_timer += 1
    if enemy_timer >= enemy_delay:
        enemy_x = random.randint(0, WIDTH - CAR_WIDTH)
        enemies.append(pygame.Rect(enemy_x, -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT))
        enemy_timer = 0

    # Move and draw enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
        draw_car(enemy.x, enemy.y, RED)

        # Check collision
        player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
        if check_collision(player_rect, enemy):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw player car
    draw_car(player_x, player_y, BLUE)

    pygame.display.flip()

pygame.quit()
