import pygame
import numpy as np
import copy
import c_components
import e_entity
import s_shipMovement
import s_renderingSystem

WIDTH = 1024
HEIGHT = 768
SHIPBASEHEALTH = 100
SHIP_SPRITE = "sprites/ship.png"
KEYS = [pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_ESCAPE]
EXPLOSION = "sprites/explosion.png"
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
dt = 0

if __name__ == "__main__":
    
    pygame.init()
    
    # self, hp, sprite, inputs, explosion):
    ship_entity = e_entity.Ship(SHIPBASEHEALTH, SHIP_SPRITE, KEYS, EXPLOSION)
    ship_system = s_shipMovement.ShipMovement()
    rendering_system = s_renderingSystem.RenderingSystem()
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        SCREEN.fill("black")

        ship_system.moveShipsAndBullets(dt, ship_entity.input_state[0], 
                                        ship_entity.bullets[0])
        #Update & Render ship
        rendering_system.render(ship_entity.input_state[0], ship_entity.sprite[0], ship_entity.bullets[0])
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()