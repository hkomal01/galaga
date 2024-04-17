import e_entity
import c_components
import pygame

class CollisionSystem:
    def checkAlienCollision(self, shipBullet_entity, alien_entity, explosion_entity, alienLock): 
        
        deleteShipBullets = [] 
        
        for m, bullet in enumerate(shipBullet_entity.movement):
            markDeathAlien = [] 
            with alienLock: 
                for i, (alien, health) in enumerate(zip(alien_entity.sprite, alien_entity.health)):
                    bullet_rect = pygame.Rect(bullet.position.x, bullet.position.y, 5, 15)
                    # make explosion for the alien to be true or just decrease 
                    # the health to 0? I'm just going to do both for now and it 
                    # may be clearer later on what to do
                    if bullet_rect.colliderect(alien.rect):
                        # change later to DELETE BULLET RIGHT AFTER COLLIDE
                        health.health -= 1
                        deleteShipBullets.append(m)
                        if health.health == 0:
                            markDeathAlien.append(i)
                        break

                for i in markDeathAlien[::-1]:
                    movement = alien_entity.movement[i]
                    explosion_entity.add_explosion((movement.position.x, movement.position.y, 0, 0))
                    del alien_entity.health[i]
                    del alien_entity.sprite[i]
                    del alien_entity.movement[i]
                    del alien_entity.cooldown[i]
                    alien_entity.num -= 1
            
        for p in deleteShipBullets[::-1]:
            del shipBullet_entity.movement[p]

    def checkShipCollision(self, alienBullet_entity, explosion_entity, ship_entity):
        
        #Ship dead
        if (ship_entity.health[0].health <= 0):
            return
        
        deleteAlienBullets = []
        
        for m, bullet in enumerate(alienBullet_entity.movement):
                #shipSprite, shipHealth
                bullet_rect = pygame.Rect(bullet.position.x, bullet.position.y, 5, 15)
                if bullet_rect.colliderect(ship_entity.sprite[0].rect):
                    # change later to DELETE BULLET RIGHT AFTER COLLIDE
                    ship_entity.health[0].health -= 1
                    deleteAlienBullets.append(m)
                    if ship_entity.health[0].health == 0:
                        explosion_entity.add_explosion((ship_entity.movement[0].position.x, 
                                                        ship_entity.movement[0].position.y, 0, 0))
                    break
        
        for b in deleteAlienBullets[::-1]:
                del alienBullet_entity.movement[b]
                
    def checkShipAlienCollision(self, alien_entity, explosion_entity, ship_entity, alienLock):
        
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
                            explosion_entity.add_explosion((ship_entity.movement[0].position.x, 
                                                            ship_entity.movement[0].position.y, 0, 0))
                        break
            
            for i in markDeathAlien[::-1]:
                movement = alien_entity.movement[i]
                explosion_entity.add_explosion((movement.position.x, movement.position.y, 0, 0))
                del alien_entity.health[i]
                del alien_entity.sprite[i]
                del alien_entity.movement[i]
                del alien_entity.cooldown[i]
                alien_entity.num -= 1