import e_entity
import c_components
import pygame
# Inputs:
# Input State of ship (has the coordinates of ship)
# All 
#def detectCollisionWithShip():


# bullets from ship hitting alien

# ship's bullets component 
# array of alien sprites
# explision comps
class CollisionSystem:
    def checkAlienCollision(self, alienHealth, alienSprite, bulletsFromShip, alien_entity, explosion_entity): 
        markDeathAlien = []
        deleteBullets = [] # ?
        # bullet hits alien
        # mark bullet
        # check alien death
        # mark alien
        # break
        # delete aliens
        
        for m, bullet in enumerate(bulletsFromShip.bullets):
            for i, (alien, health) in enumerate(zip(alienSprite, alienHealth)):
                bullet_rect = pygame.Rect(bullet.x, bullet.y, 5, 15)
                # make explosion for the alien to be true or just decrease 
                # the health to 0? I'm just going to do both for now and it 
                # may be clearer later on what to do
                if bullet_rect.colliderect(alien.rect):
                    # change later to DELETE BULLET RIGHT AFTER COLLIDE
                    health.health -= 1
                    deleteBullets.append(m)
                    if health.health == 0:
                        markDeathAlien.append(i)
                    break
        #  self.health = []
        # self.sprite = []
        # self.movement = []
        # self.bullets =[]

        # yo rn the bullets never get deleted; column mismatch
        for i in markDeathAlien[::-1]:
            movement = alien_entity.movement[i]
            explosion_entity.add_explosion((movement.position.x, movement.position.y, 0, 0))
            del alien_entity.health[i]
            del alien_entity.sprite[i]
            del alien_entity.movement[i]
            alien_entity.num -= 1
            
        for p in deleteBullets[::-1]:
            del bulletsFromShip.bullets[p]
        #delete alien
        #delete bullet

