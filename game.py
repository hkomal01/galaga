import pygame
import numpy as np
import copy
import c_components
import e_entity
import s_shipMovement
import s_alienMovement
import s_renderingSystem
import s_collisionDetection
import s_explosion
import time

WIDTH = 1024
HEIGHT = 768
SHIPBASEHEALTH = 3
SHIP_SPRITE = "sprites/ship.png"
KEYS = [pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_ESCAPE, pygame.K_p]
MOVEMENT = [WIDTH / 2, (HEIGHT / 6) *5, 300, 0]
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
dt = 0

if __name__ == "__main__":
    
    pygame.init()
    
    # self, hp, sprite, inputs, explosion):
    
    #ENTITIES
    ship_entity = e_entity.Ship(SHIPBASEHEALTH, SHIP_SPRITE, KEYS, MOVEMENT)
    aliens_entities = e_entity.Alien()
    aliens_entities.add_alien(1, "sprites/enemy1.png", (WIDTH/2, HEIGHT/2, 0, 0))
    aliens_entities.add_alien(1, "sprites/enemy2.png", (WIDTH/3, HEIGHT/2, 0, 0))
    aliens_entities.add_alien(1, "sprites/enemy3.png", (2*WIDTH/3, HEIGHT/2, 0, 0))
    aliens_entities.add_alien(1, "sprites/enemy1.png", (WIDTH/4, HEIGHT/2, 25, -5))
    aliens_entities.add_alien(1, "sprites/enemy2.png", (3*WIDTH/4, HEIGHT/2, -1, 1))
    explosion_entities = e_entity.Explosion()
    
    #SYSTEMS
    ship_system = s_shipMovement.ShipMovement()
    aliens_system = s_alienMovement.AlienMovement()
    rendering_system = s_renderingSystem.RenderingSystem()
    collision_system = s_collisionDetection.CollisionSystem()
    explosion_system = s_explosion.ExplosionSystem()
    
    
    while running and not ship_entity.input_state[0].quit:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        SCREEN.fill("black")
        
        #SYSTEM
        #MOVEMENT (Ship & Alien)
        ship_system.moveShipsAndBullets(dt, ship_entity.input_state[0], 
                                        ship_entity.bullets[0], ship_entity.movement[0])
        aliens_system.moveAliensAndBullets(dt, aliens_entities)
        
        #SYSTEM
        #EXPLOSION
        explosion_system.update(explosion_entities)
        
        #SYSTEM
        #COLLISION (Alien)
        collision_system.checkAlienCollision(aliens_entities.health, aliens_entities.sprite, ship_entity.bullets[0], aliens_entities, explosion_entities)
        
        #SYSTEM
        #RENDERING
        rendering_system.render(ship_entity.movement[0], ship_entity.sprite[0], ship_entity.bullets[0])
        for i in range(aliens_entities.num):
            rendering_system.render(aliens_entities.movement[i], aliens_entities.sprite[i], aliens_entities.bullets[i])
        for n in range(explosion_entities.num):
            rendering_system.render(explosion_entities.movement[n], explosion_entities.sprites[explosion_entities.animIndex[n]], explosion_entities.bullets[n])
        
        # flip() the display to put your work on screen
        pygame.display.flip()
            
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()