#this allows usst o use code from
#the open-source pygame library
#throughout this file
import importlib
import constants
importlib.reload(constants)

import pygame
from constants import *
from player import Player



def main():
    pygame.init()
    
    screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Player in Center")

    # create clock
    clock = pygame.time.Clock()

    # delta time  variable
    dt = 0

    # Create the player object, placing it in the center of the screen.
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player (x,y)

    # setting up the main loop (infinite Loop)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Update player (rotate based on key inputs)
        player.update(dt)
        
        # Fill the screen with a solid black color (RGB: 0, 0, 0)
        screen.fill((0, 0, 0))

        # Draw player on screen
        player.draw(screen)

        # Refresh the display
        pygame.display.flip()

        dt= clock.tick(60) / 1000 # converts miliseconds to seconds.


if __name__ == "__main__":
    main()