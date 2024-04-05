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
    def checkAlienCollision(self, alienHealth, alienExplosion, alienSprite, bulletsFromShip, alien_entity): 
        markDeathAlien = []
        deleteBullets = [] # ?
        # bullet hits alien
        # mark bullet
        # check alien death
        # mark alien
        # break
        # delete aliens
        
        for m, bullet in enumerate(bulletsFromShip.bullets):
            for i, (alien, health, explosion) in enumerate(zip(alienSprite, alienHealth, 
                                                                alienExplosion)):
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
                        explosion.is_dead = True
                    break
        #  self.health = []
        # self.sprite = []
        # self.movement = []
        # self.explosion = []
        # self.bullets =[]
        for i in markDeathAlien[::-1]:
            del alien_entity.health[i]
            del alien_entity.sprite[i]
            del alien_entity.movement[i]
            del alien_entity.explosion[i]
            alien_entity.num -= 1
            
        for p in deleteBullets[::-1]:
            del bulletsFromShip.bullets[p]
        #delete alien
        #delete bullet

