import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_SIZE = 50
PLAYER_SPEED = 5
JUMP_HEIGHT = 12
GRAVITY = 0.8

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Pygame Game")

player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
player_x_vel = 0
player_y_vel = 0
is_jumping = False

running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x_vel = -PLAYER_SPEED
    elif keys[pygame.K_d]:
        player_x_vel = PLAYER_SPEED
    else:
        player_x_vel = 0

    if keys[pygame.K_w] and not is_jumping:
        player_y_vel = -JUMP_HEIGHT
        is_jumping = True

    player_y_vel += GRAVITY

    player_x += player_x_vel
    player_y += player_y_vel

    if player_y >= SCREEN_HEIGHT - PLAYER_SIZE - 10:
        player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
        player_y_vel = 0
        is_jumping = False

    pygame.draw.rect(screen, WHITE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    pygame.display.update()

    # Limit the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
