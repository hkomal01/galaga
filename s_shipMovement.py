import pygame
import c_components
import game
import copy

class ShipMovement:
    def moveShipsAndBullets(self, dt, InputState, shipBullet_entity, Movement):
        
        #Bullet Movement & deletion
        for mov in shipBullet_entity.movement:
            mov.position.y += mov.vy * dt
            # Remove bullets that are off-screen
            if mov.position.y < -20:
                shipBullet_entity.movement.remove(mov)

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
            shipBullet_entity.add_shipBullet((player_pos.x, player_pos.y, 0, -1200))
            InputState.cooldown = InputState.cooldown_time
        
        InputState.cooldown -= dt
        InputState.update()