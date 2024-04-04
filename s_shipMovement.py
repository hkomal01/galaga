import pygame
import c_components
import game
import copy

class ShipMovement:
    def moveShipsAndBullets(self, dt, InputState, Bullets):
        
        #Bullet Movement & deletion
        for pos in Bullets.bullets:
            pos.y -= 25
            # Remove bullets that are off-screen
            if pos.y < -20:
                Bullets.bullets.remove(pos)
        
        
        #Ship Movement
        player_pos = InputState.player_pos
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
            if player_pos.x < (0 + 40):
                player_pos.x = 40
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
            if player_pos.x > (game.WIDTH - 40):
                player_pos.x = game.WIDTH - 40
        if keys[pygame.K_SPACE] and InputState.cooldown <= 0:
            Bullets.bullets.append(copy.deepcopy(InputState.player_pos))
            InputState.cooldown = InputState.cooldown_time
        
        InputState.cooldown -= dt