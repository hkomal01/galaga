import pygame
import c_components
import game
import copy

class ShipMovement:
    def moveShipsAndBullets(self, dt, InputState, Bullets):
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