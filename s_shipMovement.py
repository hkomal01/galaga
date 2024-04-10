import pygame
import c_components
import game
import copy

class ShipMovement:
    def moveShip(self, dt, ship_entity, shipBullet_entity):      
        #Ship dead
        if (ship_entity.health[0].health <= 0):
            ship_entity.input_state[0].update()
            return
    
        player_pos = ship_entity.movement[0].position
        if ship_entity.input_state[0].left:
            player_pos.x -= ship_entity.movement[0].vx * dt
            if player_pos.x < (0 + 40):
                player_pos.x = 40
        if ship_entity.input_state[0].right:
            player_pos.x += ship_entity.movement[0].vx * dt
            if player_pos.x > (game.WIDTH - 40):
                player_pos.x = game.WIDTH - 40
        if ship_entity.input_state[0].shoot and ship_entity.cooldown[0].cooldownValue <= 0:
            shipBullet_entity.add_shipBullet((player_pos.x, player_pos.y, 0, -1200))
            ship_entity.cooldown[0].cooldownValue = ship_entity.cooldown[0].cooldownTime
        
        ship_entity.cooldown[0].cooldownValue -= dt
        ship_entity.input_state[0].update()
        
    def moveShipBullets(self, dt, shipBullet_entity):
        
        #Bullet Movement & deletion
        for mov in shipBullet_entity.movement:
            mov.position.y += mov.vy * dt
            # Remove bullets that are off-screen
            if mov.position.y < -20:
                shipBullet_entity.movement.remove(mov)