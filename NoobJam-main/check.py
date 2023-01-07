import sys

import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (800, 600)

# Create the screen
screen = pygame.display.set_mode(screen_size)

# Set the font and font size
font = pygame.font.SysFont("Arial",30)

# Set the text messages
lines = ["Line 1", "Line 2", "Line 3"]

# Set the vertical spacing between lines
line_spacing = 5

# Set the starting position for the first line
x = 50
y = 50
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    font = pygame.font.Font(None, 36)

    # Set the text messages
    # lines = ["Line 1", "Line 2", "Line 3"]

    # Set the vertical spacing between lines
    line_spacing = 5

    # Set the starting position for the first line
    x = 50
    y = 50

    # Render and blit each line of text onto the screen
    for line in lines:
        text = font.render(line, True, (255, 255, 255), (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.topleft = (x, y)
        screen.blit(text, text_rect)
        y += text_rect.height + line_spacing
# Render and blit each line of text onto the screen
    pygame.display.update()

# Update the display
