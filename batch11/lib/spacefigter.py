import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Fighter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load spaceship image
SPACESHIP_IMAGE = pygame.image.load("spaceship.jfif")
SPACESHIP = pygame.transform.scale(SPACESHIP_IMAGE, (50, 50))

# Bullet settings
BULLET_SPEED = 10
bullets = []

# Spaceship settings
spaceship_x = WIDTH // 2
spaceship_y = HEIGHT - 60
spaceship_speed = 5

# Enemy settings
enemy_width, enemy_height = 50, 50
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 3
enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    WIN.fill(BLACK)

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Fire bullet
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(spaceship_x + 20, spaceship_y, 5, 10)
                bullets.append(bullet)

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship_x > 0:
        spaceship_x -= spaceship_speed
    if keys[pygame.K_RIGHT] and spaceship_x < WIDTH - 50:
        spaceship_x += spaceship_speed
    if keys[pygame.K_UP] and spaceship_y > 0:
        spaceship_y -= spaceship_speed
    if keys[pygame.K_DOWN] and spaceship_y < HEIGHT - 50:
        spaceship_y += spaceship_speed

    # Move enemy
    enemy_rect.y += enemy_speed
    if enemy_rect.y > HEIGHT:
        enemy_rect.x = random.randint(0, WIDTH - enemy_width)
        enemy_rect.y = -enemy_height

    # Check collision with bullets
    for bullet in bullets[:]:
        bullet.y -= BULLET_SPEED
        if bullet.colliderect(enemy_rect):
            bullets.remove(bullet)
            # Reset enemy
            enemy_rect.x = random.randint(0, WIDTH - enemy_width)
            enemy_rect.y = -enemy_height
        elif bullet.y < 0:
            bullets.remove(bullet)

    # Draw spaceship
    WIN.blit(SPACESHIP, (spaceship_x, spaceship_y))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(WIN, WHITE, bullet)

    # Draw enemy
    pygame.draw.rect(WIN, RED, enemy_rect)

    pygame.display.update()

pygame.quit()
sys.exit()
