import pygame
import sys
import math
from finalScreen import finalScreen

def game(screen, background_image, player_images):
    # Constants
    surface = pygame.Surface((20, 20))
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    WHITE = (255, 255, 255)
    PLAYER_SIZE = 100
    PLAYER_SPEED = 5
    PLAYER_JUMP = 50
    OBJECTS = [(270, 230), (525, 400), (500, 270), (715, 500), (250, SCREEN_HEIGHT - 185)]
    COLLISION_RADIUS = 20

    # Initialize Pygame mixer for sound
    pygame.mixer.init()
    
    # Load sounds
    pygame.mixer.music.load("rain-in-the-city-8017.mp3")
    pygame.mixer.music.set_volume(0.3)  # Set volume for background music
    pygame.mixer.music.play(-1)  # Loop the background music

    # Player variables
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - PLAYER_SIZE - 10
    player_x_vel = 0
    player_y_vel = 0
    current_player_image = player_images["idleR"]

    # Font setup
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)

    # Introduction text
    introduction_text = "You wake up after a long night. Objective: Explore...Press C to Continue"
    introduction_box = pygame.Rect(10, 10, SCREEN_WIDTH - 20, 40)
    introduction_surface = font.render(introduction_text, True, (0, 0, 0))
    introduction_rect = introduction_surface.get_rect(center=introduction_box.center)
    show_introduction = True

    # Load health and hunger images
    health_image = pygame.image.load("health1.png").convert_alpha()
    hunger_image = pygame.image.load("hunger1.png").convert_alpha()

    # Scale health and hunger images
    health_image = pygame.transform.scale(health_image, (100, 100))
    hunger_image = pygame.transform.scale(hunger_image, (100, 100))

    # Positions of health and hunger images
    health_pos = (50, SCREEN_HEIGHT - 120)
    hunger_pos = (50, SCREEN_HEIGHT - 200)

    sleep_img = pygame.image.load("sleep.png").convert_alpha()
    sleep_img = pygame.transform.scale(sleep_img, (130, 135))
    sleep_pos = (300, SCREEN_HEIGHT - 200)

    dawg_img = pygame.image.load("dawgWHAT.png").convert_alpha()
    dawg_img = pygame.transform.scale(dawg_img, (80, 80))  # Adjust size to 80% of original
    dawg_pos = (240, SCREEN_HEIGHT - 200)

    # Variable to track the clicked object
    clicked_object = None

    # Variable to track the visibility of extra text
    show_extra_text = False
    adopted_dog = False  # Flag to track if the dog has been adopted

    def draw_objects():
        for obj in OBJECTS:
            if obj == (715, 500):
                pygame.draw.circle(surface, (0, 0, 0), obj, 65)
            else:
                pygame.draw.circle(surface, (0, 0, 0), obj, 25)

    def check_collision_with_objects(player_rect, x_vel, y_vel):
        for obj in OBJECTS:
            obj_rect = pygame.Rect(obj[0] - COLLISION_RADIUS, obj[1] - COLLISION_RADIUS, 2 * COLLISION_RADIUS, 2 * COLLISION_RADIUS)
            if player_rect.colliderect(obj_rect):
                # Calculate the direction vector from the player to the object
                direction = pygame.math.Vector2(obj[0] - player_rect.centerx, obj[1] - player_rect.centery)

                # Calculate the distance between player and object
                distance = direction.length()

                # Normalize the direction vector
                if distance != 0:
                    direction.normalize_ip()

                # Calculate the movement vector
                movement_vector = pygame.math.Vector2(x_vel, y_vel)

                # If player is moving towards the object, allow movement
                if movement_vector.dot(direction) > 0:
                    return True
        return False

    def check_mouse_collision_with_objects(mouse_pos):
        for index, obj in enumerate(OBJECTS):
            distance = math.hypot(mouse_pos[0] - obj[0], mouse_pos[1] - obj[1])
            if distance <= COLLISION_RADIUS:
                return index  # Return the index of the object that was clicked
        return None

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)

        # Blit the background image
        screen.blit(background_image, (0, 0))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    if show_introduction:
                        show_introduction = False
                    else:
                        show_extra_text = False
                        if adopted_dog:
                            # Check if the text for feeding the dog is displayed
                            if clicked_object == 4:
                                finalScreen(screen)  # Call final screen if adopted dog and text box closed
                                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_index = check_mouse_collision_with_objects(mouse_pos)
                if clicked_index is not None:
                    show_extra_text = True
                    clicked_object = clicked_index

                    # If the dog is clicked and not adopted yet
                    if clicked_object == 1 and not adopted_dog:
                        # Set the adopted_dog flag to True
                        adopted_dog = True
                        pass
                    elif clicked_object == 2:
                        pass
                    elif clicked_object == 3:
                        pass
                    elif clicked_object == 4:
                        pass

        # Draw introduction text box
        if show_introduction:
            pygame.draw.rect(screen, (200, 200, 200), introduction_box)
            screen.blit(introduction_surface, introduction_rect)

        # Handle player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not check_collision_with_objects(pygame.Rect(player_x - PLAYER_SPEED, player_y, PLAYER_SIZE, PLAYER_SIZE), -PLAYER_SPEED, 0):
            player_x_vel = -PLAYER_SPEED
            current_player_image = player_images["walkL"]
        elif keys[pygame.K_d] and not check_collision_with_objects(pygame.Rect(player_x + PLAYER_SPEED, player_y, PLAYER_SIZE, PLAYER_SIZE), PLAYER_SPEED, 0):
            player_x_vel = PLAYER_SPEED
            current_player_image = player_images["walkR"]
        else:
            player_x_vel = 0
            if player_x_vel < 0:
                current_player_image = player_images["idleL"]
            else:
                current_player_image = player_images["idleR"]

        if keys[pygame.K_w] and not check_collision_with_objects(pygame.Rect(player_x, player_y - PLAYER_SPEED, PLAYER_SIZE, PLAYER_SIZE), 0, -PLAYER_SPEED):
            player_y -= PLAYER_SPEED
        elif keys[pygame.K_s] and not check_collision_with_objects(pygame.Rect(player_x, player_y + PLAYER_SPEED, PLAYER_SIZE, PLAYER_SIZE), 0, PLAYER_SPEED):
            player_y += PLAYER_SPEED

        # Update player position
        player_x += player_x_vel

        # Draw Sleeping
        screen.blit(sleep_img, sleep_pos)

        # Draw the player
        screen.blit(current_player_image, (player_x, player_y))

        # Draw objects
        draw_objects()

        # Draw health and hunger
        screen.blit(health_image, health_pos)
        screen.blit(hunger_image, hunger_pos)

        # Always draw the dog if adopted
        if adopted_dog:
            screen.blit(dawg_img, dawg_pos)

        # Show text based on clicked object
        if show_extra_text and clicked_object is not None:
            if clicked_object == 0:
                text = "Hmm...There's nothing inside."
            elif clicked_object == 1:
                text = "Wow! There's a dog inside... It looks hungry... You decide to adopt it."
            elif clicked_object == 2:
                text = "Wow! Looks like there's some money here! You can buy food!"
            elif clicked_object == 3:
                text = "Hmm... Looks like the passage is blocked by boxes"
            elif clicked_object == 4:
                text = "The dog looks hungry. You feed it food. No food for yourself now..."
            else:
                text = ""

            box = pygame.Rect(10, 10, SCREEN_WIDTH - 20, 40)
            surface = font.render(text, True, (0, 0, 0))
            rect = surface.get_rect(center=box.center)
            pygame.draw.rect(screen, (200, 200, 200), box)
            screen.blit(surface, rect)

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        pygame.time.Clock().tick(60)

    pygame.mixer.music.stop()  # Stop the background music when the game ends
    pygame.quit()
    sys.exit()

def start_screen(screen):
    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    WHITE = (255, 255, 255)
    TITLE_FONT = pygame.font.SysFont("Arial", 60)
    BUTTON_FONT = pygame.font.SysFont("Arial", 40)

    # Load background image
    background_image = pygame.image.load("home.png")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    # Title text
    title_text = "GAME"
    title_surface = TITLE_FONT.render(title_text, True, (0, 0, 0))
    title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))

    # Button text
    button_text = "Play"
    button_surface = BUTTON_FONT.render(button_text, True, (255, 255, 255))
    button_rect = button_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Game loop
    running = True
    while running:
        screen.fill(WHITE)

        # Blit the background image
        screen.blit(background_image, (0, 0))

        # Draw title and button
        screen.blit(title_surface, title_rect)
        screen.blit(button_surface, button_rect)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    return

        # Update the display
        pygame.display.update()

def main():
    # Initialize Pygame
    pygame.init()

    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    WHITE = (255, 255, 255)

    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Experiencing Homelessness")

    # Run start screen
    start_screen(screen)

    # Load player images
    player_images = {
        "idleR": pygame.image.load("characters/idleR.png").convert_alpha(),
        "idleL": pygame.image.load("characters/idleL.png").convert_alpha(),
        "walkR": pygame.image.load("characters/walkR.png").convert_alpha(),
        "walkL": pygame.image.load("characters/walkL.png").convert_alpha(),
    }

    # Scale player images
    for key, image in player_images.items():
        player_images[key] = pygame.transform.scale(image, (100, 100))

    # Run the jump game
    run_jump_game(screen, background_image, player_images)

if __name__ == "__main__":
    main()
