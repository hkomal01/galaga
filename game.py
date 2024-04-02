import pygame
import numpy as np
import copy
import c_components
import e_entity

pygame.init()
width = 1024
height = 768
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
dt = 0
cooldown = 0
cooldown_time = .1

ship_c_sprite = c_components.Sprite("sprites/ship.png")
ship = e_entity.Ship()
ship.addSprite(ship_c_sprite)

player_pos = pygame.Vector2(screen.get_width() / 2, (screen.get_height() / 6) *5)

bullets = []

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
        if player_pos.x < (0 + 40):
            player_pos.x = 40
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        if player_pos.x > (width - 40):
            player_pos.x = width - 40
    if keys[pygame.K_SPACE] and cooldown <= 0:
        bullets.append(copy.deepcopy(player_pos))
        cooldown = cooldown_time
    
    cooldown -= dt

        
    #Update & Render ship
    ship.sprite[0].update(player_pos)
    screen.blit(ship.sprite[0].image, ship.sprite[0].rect)

    for pos in bullets:
        pygame.draw.rect(screen, "red", pygame.Rect(pos.x, pos.y, 5, 15))
        pos.y -= 25
        # Remove bullets that are off-screen
        if pos.y < -20:
            bullets.remove(pos)
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
