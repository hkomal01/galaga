import e_entity
import c_components
import copy

class AlienMovement:
    def moveAliens(self, dt, aliens_entities, alienBullet_entity):
        for _ in range(aliens_entities.num):
            for move in aliens_entities.movement:
                alienBullet_entity.add_alienBullet((move.position.x, move.position.y, 0, 1200))
                move.position.x += dt * move.vx
                move.position.y += dt * move.vy

    def moveAlienBullets(self, dt, alienBullet_entity):
        #Bullet Movement & deletion
        for mov in alienBullet_entity.movement:
            mov.position.y += dt * mov.vy
            # Remove bullets that are off-screen
            if mov.position.y < -20:
                alienBullet_entity.remove(mov)


            
