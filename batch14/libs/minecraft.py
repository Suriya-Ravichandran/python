import pygame
import sys

# Initialize
pygame.init()

# Constants
TILE_SIZE = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE

# Colors
DIRT = (155, 118, 83)
GRASS = (106, 190, 48)
SKY = (135, 206, 235)
WHITE = (255, 255, 255)

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Minecraft 2D")

clock = pygame.time.Clock()

# World data (initially empty)
world = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Player cursor
cursor_x, cursor_y = 0, 0

# Selected block type
selected_block = "grass"

# Game loop
running = True
while running:
    screen.fill(SKY)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Movement
            elif event.key == pygame.K_LEFT:
                cursor_x = max(cursor_x - 1, 0)
            elif event.key == pygame.K_RIGHT:
                cursor_x = min(cursor_x + 1, GRID_WIDTH - 1)
            elif event.key == pygame.K_UP:
                cursor_y = max(cursor_y - 1, 0)
            elif event.key == pygame.K_DOWN:
                cursor_y = min(cursor_y + 1, GRID_HEIGHT - 1)

            # Block placing
            elif event.key == pygame.K_SPACE:
                world[cursor_y][cursor_x] = selected_block

            # Block breaking
            elif event.key == pygame.K_BACKSPACE:
                world[cursor_y][cursor_x] = None

            # Switch block types
            elif event.key == pygame.K_1:
                selected_block = "grass"
            elif event.key == pygame.K_2:
                selected_block = "dirt"

    # Draw world
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            block = world[y][x]
            if block == "grass":
                pygame.draw.rect(screen, GRASS, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif block == "dirt":
                pygame.draw.rect(screen, DIRT, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw cursor
    pygame.draw.rect(screen, WHITE, (cursor_x * TILE_SIZE, cursor_y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 3)

    # Update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
