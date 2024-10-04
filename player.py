import importlib
import constants
importlib.reload(constants)

import pygame
from pygame.math import Vector2
from constants import *


#Referencing CircleShape from circleshape.py

class CircleShape:
    def __init__(self, x, y, radius):
        self.position= Vector2(x,y)
        self.radius = radius

    def draw(self, screen):
        #overwridden by subclasses
        pass
# Player Class

class Player(CircleShape):
    PLAYER_RADIUS = PLAYER_RADIUS #player radius

    def __init__(self, x, y):
        #call parent class, feed it x, y, and radius
        super().__init__(x,y, self.PLAYER_RADIUS)
        self.rotation = 0 #set player rotation to 0

    #Roate the player

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    #Move the player

    def move(self,dt):
        direction_vector = Vector2(0,1)
        direction_vector= direction_vector.rotate(self.rotation)
        movement_vector = direction_vector * PLAYER_SPEED * dt
        self.position += movement_vector

    # Update method

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #Roate Left (invert dt to rotate counter-clockwise)
            self.rotate(-dt)
        if keys[pygame.K_d]:
            #Rotate right (clockwise- positive dt)
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)


    # Triangle mehtod

    def triangle(self):
        forward= pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation +90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #Override the draw method
    def draw(self,screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

