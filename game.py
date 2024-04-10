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
COOLDOWN = 0.18
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
dt = 0

if __name__ == "__main__":
    
    pygame.init()
    
    #ENTITIES
    ship_entity = e_entity.Ship(SHIPBASEHEALTH, SHIP_SPRITE, KEYS, MOVEMENT, COOLDOWN)
    shipBullet_entity = e_entity.ShipBullet()
    
    aliens_entities = e_entity.Alien()
    aliens_entities.add_alien(1, "sprites/enemy1.png", (1 * WIDTH / 6, HEIGHT / 2, 1, -5), 1)
    aliens_entities.add_alien(1, "sprites/enemy2.png", (2 * WIDTH / 6, HEIGHT / 2, 1, -4), 1.5)
    #aliens_entities.add_alien(1, "sprites/enemy3.png", (3 * WIDTH / 6, HEIGHT/2, 1, -3), .75)
    aliens_entities.add_alien(1, "sprites/enemy1.png", (4 * WIDTH / 6, HEIGHT / 2, 1, -2), 3)
    aliens_entities.add_alien(1, "sprites/enemy2.png", (5 * WIDTH / 6, HEIGHT / 2, 1, -1), 2)
    alienBullet_entity = e_entity.AlienBullet()
    
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
        ship_system.moveShip(dt, ship_entity, shipBullet_entity)
        ship_system.moveShipBullets(dt, shipBullet_entity)
        
        aliens_system.moveAliens(dt, aliens_entities, alienBullet_entity)
        aliens_system.moveAlienBullets(dt, alienBullet_entity)

        #SYSTEM
        #EXPLOSION
        explosion_system.update(explosion_entities)
        
        #SYSTEM
        #COLLISION (Alien)
        collision_system.checkAlienCollision(shipBullet_entity, 
                                             aliens_entities, 
                                             explosion_entities)
        collision_system.checkShipCollision(alienBullet_entity,
                                             explosion_entities, 
                                             ship_entity)
        
        #SYSTEM
        #RENDERING
        if ship_entity.health[0].health > 0:
            rendering_system.render(ship_entity.movement[0], ship_entity.sprite[0])
    
        for i in range(aliens_entities.num):
            rendering_system.render(aliens_entities.movement[i],
                                     aliens_entities.sprite[i])
        
        for n in range(explosion_entities.num):
            rendering_system.render(explosion_entities.movement[n], 
                                    explosion_entities.sprites
                                    [explosion_entities.animIndex[n]])
        #Render bullets
        rendering_system.renderBullets(shipBullet_entity, alienBullet_entity)

        # flip() the display to put your work on screen
        pygame.display.flip()
            
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()