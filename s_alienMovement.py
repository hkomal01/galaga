import e_entity
import c_components
import copy

class AlienMovement:
    def moveAliens(self, dt, aliens_entities, alienBullet_entity, frame_count):
        for i, move in enumerate(aliens_entities.movement):
            #alienBullet_entity.add_alienBullet((move.position.x, move.position.y, 0, 1200))
            if move.fn != None:
                (x, y, inc) = move.fn(move)
                move.position.x = x
                move.position.y = y
                move.t += inc * dt
            else:
                move.position.x += dt * move.vx
                move.position.y += dt * move.vy
            if aliens_entities.cooldown[i].cooldownValue <= 0:
                alienBullet_entity.add_alienBullet((move.position.x, move.position.y, 0, 800))
                aliens_entities.cooldown[i].cooldownValue = aliens_entities.cooldown[i].cooldownTime
            aliens_entities.cooldown[i].cooldownValue -= dt

    def moveAlienBullets(self, dt, alienBullet_entity):
        #Bullet Movement & deletion
        for mov in alienBullet_entity.movement:
            mov.position.y += dt * mov.vy
            # Remove bullets that are off-screen
            if mov.position.y < -20:
                alienBullet_entity.movement.remove(mov)


            
