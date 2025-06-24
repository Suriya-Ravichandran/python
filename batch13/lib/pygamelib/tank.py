import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Fight")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN = (0, 180, 0)
BLACK = (0, 0, 0)

# Tank settings
TANK_SIZE = (40, 60)
BULLET_SPEED = 7
TANK_SPEED = 3
ROTATE_SPEED = 5
MAX_HEALTH = 5

clock = pygame.time.Clock()

# Tank class
class Tank:
    def __init__(self, x, y, color, controls):
        self.x = x
        self.y = y
        self.angle = 0
        self.color = color
        self.controls = controls
        self.health = MAX_HEALTH
        self.bullets = []

    def draw(self):
        rotated_image = pygame.Surface(TANK_SIZE)
        rotated_image.fill(self.color)
        rotated_image = pygame.transform.rotate(rotated_image, self.angle)
        rect = rotated_image.get_rect(center=(self.x, self.y))
        screen.blit(rotated_image, rect.topleft)

        # Health Bar
        pygame.draw.rect(screen, RED, (self.x - 25, self.y + 40, 50, 5))
        pygame.draw.rect(screen, GREEN, (self.x - 25, self.y + 40, 10 * self.health, 5))

    def move(self, keys):
        if keys[self.controls["left"]]:
            self.angle += ROTATE_SPEED
        if keys[self.controls["right"]]:
            self.angle -= ROTATE_SPEED
        if keys[self.controls["forward"]]:
            self.x += TANK_SPEED * math.cos(math.radians(-self.angle))
            self.y += TANK_SPEED * math.sin(math.radians(-self.angle))
        if keys[self.controls["backward"]]:
            self.x -= TANK_SPEED * math.cos(math.radians(-self.angle))
            self.y -= TANK_SPEED * math.sin(math.radians(-self.angle))

    def shoot(self):
        bullet_dx = math.cos(math.radians(-self.angle))
        bullet_dy = math.sin(math.radians(-self.angle))
        bullet = {
            "x": self.x,
            "y": self.y,
            "dx": bullet_dx * BULLET_SPEED,
            "dy": bullet_dy * BULLET_SPEED
        }
        self.bullets.append(bullet)

    def update_bullets(self, other_tank):
        for bullet in self.bullets[:]:
            bullet["x"] += bullet["dx"]
            bullet["y"] += bullet["dy"]
            pygame.draw.circle(screen, BLACK, (int(bullet["x"]), int(bullet["y"])), 4)

            # Collision check
            if abs(bullet["x"] - other_tank.x) < 30 and abs(bullet["y"] - other_tank.y) < 30:
                other_tank.health -= 1
                self.bullets.remove(bullet)
            elif not (0 <= bullet["x"] <= WIDTH and 0 <= bullet["y"] <= HEIGHT):
                self.bullets.remove(bullet)

# Controls
controls1 = {"left": pygame.K_a, "right": pygame.K_d, "forward": pygame.K_w, "backward": pygame.K_s, "shoot": pygame.K_SPACE}
controls2 = {"left": pygame.K_LEFT, "right": pygame.K_RIGHT, "forward": pygame.K_UP, "backward": pygame.K_DOWN, "shoot": pygame.K_RCTRL}

# Create tanks
tank1 = Tank(200, 300, RED, controls1)
tank2 = Tank(600, 300, GREEN, controls2)

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Shooting
        if event.type == pygame.KEYDOWN:
            if event.key == tank1.controls["shoot"]:
                tank1.shoot()
            if event.key == tank2.controls["shoot"]:
                tank2.shoot()

    tank1.move(keys)
    tank2.move(keys)

    tank1.update_bullets(tank2)
    tank2.update_bullets(tank1)

    tank1.draw()
    tank2.draw()

    if tank1.health <= 0 or tank2.health <= 0:
        font = pygame.font.SysFont(None, 80)
        winner = "Green Wins!" if tank1.health <= 0 else "Red Wins!"
        text = font.render(winner, True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 40))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()

pygame.quit()
