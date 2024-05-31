import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BUTTON_COLOR = (0, 200, 100)
BUTTON_HOVER_COLOR = (0, 255, 150)
FONT = pygame.font.Font(None, 60)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Experiencing Homeslessness")

# Load background images
background = "home"
background_image_home = pygame.image.load("home.png")
background_image_home = pygame.transform.scale(background_image_home, (SCREEN_WIDTH, SCREEN_HEIGHT))

background_image_game = pygame.image.load("FirstBackground.png")
background_image_game = pygame.transform.scale(background_image_game, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load player images
character_folder = "characters"
player_images = {
    "idleR": pygame.image.load(os.path.join(character_folder, "idleR.png")),
    "idleL": pygame.image.load(os.path.join(character_folder, "idleL.png")),
    "walkR": pygame.image.load(os.path.join(character_folder, "walkR.png")),
    "walkL": pygame.image.load(os.path.join(character_folder, "walkL.png"))
}

# Scale player images
for key in player_images:
    player_images[key] = pygame.transform.scale(player_images[key], (100, 100))

# Player variables
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT - 100 - 10
player_x_vel = 0
player_y_vel = 0
current_player_image = player_images["idleR"]  # Start with idle right

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Function to check if a point is inside a rectangle
def is_inside_rect(x, y, rect):
    return rect.left <= x <= rect.right and rect.top <= y <= rect.bottom

# Function to run the jump game
def run_jump_game():
    from main import game
    game(screen, background_image_game, player_images)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    # Draw background based on the state
    if background == "home":
        screen.blit(background_image_home, (0, 0))
    elif background == "game":
        screen.blit(background_image_game, (0, 0))

    # Draw Title
    draw_text("Experiencing Homelessness", FONT, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)

    # Draw Play button
    play_button = pygame.Rect(300, 400, 200, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, play_button)
    draw_text("Play", FONT, WHITE, screen, 400, 425)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if is_inside_rect(mouse_x, mouse_y, play_button):
                run_jump_game()
                background = "game"  # Change the background to game

    # Change button color on hover
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if is_inside_rect(mouse_x, mouse_y, play_button):
        pygame.draw.rect(screen, BUTTON_HOVER_COLOR, play_button)
        draw_text("Play", FONT, WHITE, screen, 400, 425)

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()
