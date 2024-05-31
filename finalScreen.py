import pygame
import sys

def finalScreen(screen):
    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont("Arial", 24)
    big_font = pygame.font.SysFont("Arial", 60)

    # Texts
    texts = [
        "One in every 500 Americans is experiencing homelessness.",
        "That's over 600,000 people.",
        "",
        "Through the years that they are on the streets,",
        "The battle against hunger, bad weather, violence, loneliness..",
        "All things that no human should ever have to go through.",
        "They don't have to be alone.",
        "",
        "By volunteering at homeless shelters, soup kitchens,",
        "Giving money, or even just by saying good morning,",
        "You can make a difference in the battle against homelessness.",
        "A Special Thank you to the Friendship Place and other organizations",
        "that are working daily to support people experiencing homelessness.",
        "These places are amazing, yet there are blockades such as money.",
        "If you want to help with the cause, visit our donation page.",
        "",
        "Ending Homelessness, and Building Lives"
    ]

    # Create surfaces for each line of text
    text_surfaces = [font.render(text, True, WHITE) for text in texts]
    text_rects = [text_surface.get_rect(center=(SCREEN_WIDTH // 2, y)) for y, text_surface in enumerate(text_surfaces, 50)]

    # Game loop
    running = True
    index = 0  # Start displaying text from index 0
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    index += 1
                    if index >= len(texts):
                        pygame.quit()
                        sys.exit()

        # Display the text
        screen.blit(text_surfaces[index], text_rects[index])

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        pygame.time.Clock().tick(60)
