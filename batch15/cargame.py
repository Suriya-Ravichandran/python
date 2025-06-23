import pygame
import random

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH = 400
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Rider")

# Load assets
player_img = pygame.image.load("player_car.png")
enemy_img = pygame.image.load("enemy_car.png")

# Resize if needed
player_img = pygame.transform.scale(player_img, (100, 100))
enemy_img = pygame.transform.scale(enemy_img, (100, 100))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game Variables
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 120
player_speed = 5

enemy_x = random.randint(50, WIDTH - 100)
enemy_y = -100
enemy_speed = 7

score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_window():
    win.fill((50, 50, 50))  # Road color
    win.blit(player_img, (player_x, player_y))
    win.blit(enemy_img, (enemy_x, enemy_y))
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))
    pygame.display.update()

def check_collision(px, py, ex, ey):
    return px < ex + 50 and px + 50 > ex and py < ey + 100 and py + 100 > ey

# Main game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Move enemy
    enemy_y += enemy_speed

    # Respawn enemy
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(50, WIDTH - 100)
        score += 1
        enemy_speed += 0.2  # Increase difficulty

    # Check collision
    if check_collision(player_x, player_y, enemy_x, enemy_y):
        print("Game Over! Final Score:", score)
        running = False

    # Draw
    draw_window()

pygame.quit()
