import pygame
import c_components
import game
import copy

class ShipMovement:
    def moveShipsAndBullets(self, dt, InputState, Bullets, Movement):
        
        #Bullet Movement & deletion
        for pos in Bullets.bullets:
            pos.y -= 25
            # Remove bullets that are off-screen
            if pos.y < -20:
                Bullets.bullets.remove(pos)

        #Ship Movement
        player_pos = Movement.position
        if InputState.left:
            player_pos.x -= Movement.vx * dt
            if player_pos.x < (0 + 40):
                player_pos.x = 40
        if InputState.right:
            player_pos.x += Movement.vx * dt
            if player_pos.x > (game.WIDTH - 40):
                player_pos.x = game.WIDTH - 40
        if InputState.shoot and InputState.cooldown <= 0:
            Bullets.bullets.append(copy.deepcopy(Movement.position))
            InputState.cooldown = InputState.cooldown_time
        
        InputState.cooldown -= dt
        InputState.update()