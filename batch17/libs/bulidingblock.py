import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BRICK_COLOR = (200, 0, 0)
PADDLE_COLOR = (0, 100, 255)
BALL_COLOR = (0, 255, 100)

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 8

# Ball settings
BALL_SIZE = 15
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = 4 * random.choice((1, -1))
ball_speed_y = -4

# Brick settings
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30

bricks = []
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT + 40, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
        bricks.append(brick)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.x += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Wall collision
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Paddle collision
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Brick collision
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        hit_brick = bricks.pop(hit_index)
        ball_speed_y *= -1

    # Lose condition
    if ball.bottom >= HEIGHT:
        font = pygame.font.SysFont(None, 60)
        text = font.render("Game Over!", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Win condition
    if not bricks:
        font = pygame.font.SysFont(None, 60)
        text = font.render("You Win!", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    # Draw paddle
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)

    # Draw ball
    pygame.draw.ellipse(screen, BALL_COLOR, ball)

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
