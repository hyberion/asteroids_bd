#this allows usst o use code from
#the open-source pygame library
#throughout this file

import pygame
from constants import *

def main():
    pygame.init()
    
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # create clock
    clock = pygame.time.Clock()

    # delta time  variable
    dt = 0

    # setting up the main loop (infinite Loop)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill the screen with a solid black color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Refresh the display
        pygame.display.flip()

        dt= clock.tick(60) / 1000 # converts miliseconds to seconds.


if __name__ == "__main__":
    main()