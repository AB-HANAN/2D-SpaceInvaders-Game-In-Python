import pygame
import math
import os

pygame.init()

# clock = pygame.time.Clock()
# FPS = 60

# SCREEN_WIDTH = 1500
# SCREEN_HEIGHT = 600

# #create game window
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Endless Scroll")

# #load image
# bg = pygame.image.load(os.path.join("Images","bg.png")).convert()
# bg_width = bg.get_width()
# bg_rect = bg.get_rect()

# #define game variables
# scroll = 0
# tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1

# #game loop
# run = True
# while run:

#   clock.tick(FPS)

#   #draw scrolling background
#   for i in range(0, tiles):
#     screen.blit(bg, (i * bg_width + scroll, 0))
#     bg_rect.x = i * bg_width + scroll
#     pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

#   #scroll background
#   scroll -= 5

#   #reset scroll
#   if abs(scroll) > bg_width:
#     scroll = 0

#   #event handler
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False

#   pygame.display.update()

# pygame.quit()
import pygame
import os

# Set up the window
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the background image
BACKGROUND = pygame.image.load(os.path.join("Images", "bg21.png")).convert()

# Set up the initial positions of the two background images
bg_y1 = 0
bg_y2 = -BACKGROUND.get_height()

# Set the scrolling speed
scroll_speed = 10

def scroll_background():
    global bg_y1, bg_y2
    
    # Scroll the backgrounds vertically
    bg_y1 += scroll_speed
    bg_y2 += scroll_speed
    
    # If the first background image has scrolled off the screen, reset its position
    if bg_y1 >= HEIGHT:
        bg_y1 = -BACKGROUND.get_height()
    
    # If the second background image has scrolled off the screen, reset its position
    if bg_y2 >= HEIGHT:
        bg_y2 = -BACKGROUND.get_height()

def draw_window():
    # Draw the two background images
    WIN.blit(BACKGROUND, (0, bg_y1))
    WIN.blit(BACKGROUND, (0, bg_y2))

    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        scroll_background()
        draw_window()

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    main()
