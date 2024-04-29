import pygame
import game

class ShipMovement:
    """
    This class handles the movement of the ship and ship bullets in the game.
    """

    def moveShip(self, dt, ship_entity, shipBullet_entity):      
        """
        Moves the ship based on user input and updates the ship's cooldown.

        Args:
            dt (float): The time elapsed since the last frame.
            ship_entity (ShipEntity): The ship entity object.
            shipBullet_entity (ShipBulletEntity): The ship bullet entity object.
        """
        # Ship dead
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
        if ship_entity.input_state[0].shoot and \
                    ship_entity.cooldown[0].cooldownValue <= 0:
            shipBullet_entity.add_shipBullet((player_pos.x, 
                                                player_pos.y, 0, -1200))
            ship_entity.cooldown[0].cooldownValue = \
                                            ship_entity.cooldown[0].cooldownTime
            gun_sound = pygame.mixer.Sound("sounds/playerGun.mp3")
            pygame.mixer.Sound.play(gun_sound)

        
        ship_entity.cooldown[0].cooldownValue -= dt
        ship_entity.input_state[0].update()
        
    def moveShipBullets(self, dt, shipBullet_entity):
        """
        Moves the ship bullets and removes bullets that are off-screen.

        Args:
            dt (float): The time elapsed since the last frame.
            shipBullet_entity (ShipBulletEntity): The ship bullet entity object.
        """
        # Bullet Movement & deletion
        for mov in shipBullet_entity.movement:
            mov.position.y += mov.vy * dt
            # Remove bullets that are off-screen
            if mov.position.y < -20:
                shipBullet_entity.movement.remove(mov)