import pygame

class CollisionSystem:
    """
    A class that handles collision detection and resolution in the game.
    """

    def checkAlienCollision(self, ship_entity, shipBullet_entity, 
                                alien_entity, explosion_entity, alienLock): 
        """
        Checks for collision between ship bullets and aliens, and performs 
        necessary actions.

        Args:
            ship_entity (ShipEntity): The ship entity.
            shipBullet_entity (ShipBulletEntity): The ship bullet entity.
            alien_entity (AlienEntity): The alien entity.
            explosion_entity (ExplosionEntity): The explosion entity.
            alienLock (Lock): The lock for synchronizing access to alien entity.

        Returns:
            None
        """
        
        deleteShipBullets = [] 
        
        for m, bullet in enumerate(shipBullet_entity.movement):
            markDeathAlien = [] 
            with alienLock: 
                for i, (alien, health) in enumerate(zip(alien_entity.sprite, 
                                                        alien_entity.health)):
                    bullet_rect = pygame.Rect(bullet.position.x, 
                                                bullet.position.y, 5, 15)
                    if bullet_rect.colliderect(alien.rect):
                        health.health -= 1
                        deleteShipBullets.append(m)
                        if health.health == 0:
                            markDeathAlien.append(i)
                        break

                for i in markDeathAlien[::-1]:
                    movement = alien_entity.movement[i]
                    explosion_entity.add_explosion((movement.position.x, 
                                                     movement.position.y, 0, 0))
                    del alien_entity.health[i]
                    del alien_entity.sprite[i]
                    del alien_entity.movement[i]
                    del alien_entity.cooldown[i]
                    alien_entity.num -= 1
                    ship_entity.points[0].update()
            
        for p in deleteShipBullets[::-1]:
            del shipBullet_entity.movement[p]

    def checkShipCollision(self, alienBullet_entity, 
                                explosion_entity, ship_entity):
        """
        Checks for collision between alien bullets and the ship, 
        and performs necessary actions.

        Args:
            alienBullet_entity (AlienBulletEntity): The alien bullet entity.
            explosion_entity (ExplosionEntity): The explosion entity.
            ship_entity (ShipEntity): The ship entity.

        Returns:
            None
        """
        #Ship dead
        if (ship_entity.health[0].health <= 0):
            return
        
        deleteAlienBullets = []
        
        for m, bullet in enumerate(alienBullet_entity.movement):
                #shipSprite, shipHealth
                bullet_rect = pygame.Rect(bullet.position.x, 
                                           bullet.position.y, 5, 15)
                if bullet_rect.colliderect(ship_entity.sprite[0].rect):
                    # change later to DELETE BULLET RIGHT AFTER COLLIDE
                    ship_entity.health[0].health -= 1
                    deleteAlienBullets.append(m)
                    if ship_entity.health[0].health == 0:
                        explosion_entity.add_explosion(
                            (ship_entity.movement[0].position.x, 
                                    ship_entity.movement[0].position.y, 0, 0))
                    break
        
        for b in deleteAlienBullets[::-1]:
                del alienBullet_entity.movement[b]
                
    def checkShipAlienCollision(self, alien_entity, explosion_entity, 
                                                    ship_entity, alienLock):
        """
        Checks for collision between the ship and aliens, 
        and performs necessary actions.

        Args:
            alien_entity (AlienEntity): The alien entity.
            explosion_entity (ExplosionEntity): The explosion entity.
            ship_entity (ShipEntity): The ship entity.
            alienLock (Lock): The lock for synchronizing access to alien entity.

        Returns:
            None
        """
        #Ship dead
        if (ship_entity.health[0].health <= 0):
            return
        
        markDeathAlien = []
        
        with alienLock:
            for i, alien in enumerate(alien_entity.sprite):
                    ship_rect = ship_entity.sprite[0].rect
                    if ship_rect.colliderect(alien.rect):
                        # ship and alien collision happened
                        ship_entity.health[0].health -= 1
                        markDeathAlien.append(i)
                        if ship_entity.health[0].health == 0:
                            explosion_entity.add_explosion(
                                (ship_entity.movement[0].position.x, 
                                    ship_entity.movement[0].position.y, 0, 0))
                        break
            
            for i in markDeathAlien[::-1]:
                movement = alien_entity.movement[i]
                explosion_entity.add_explosion((movement.position.x, 
                                                movement.position.y, 0, 0))
                del alien_entity.health[i]
                del alien_entity.sprite[i]
                del alien_entity.movement[i]
                del alien_entity.cooldown[i]
                alien_entity.num -= 1
                ship_entity.points[0].update()