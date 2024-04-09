import e_entity
import c_components
import math

class AlienMovement:
    def moveAliensAndBullets(self, dt, aliens, t):
        for i in range(aliens.num):
            #Bullet Movement & deletion
            for pos in aliens.bullets[i].bullets:
                pos.y -= 25
                # Remove bullets that are off-screen
                if pos.y < -20:
                    aliens.bullets[i].bullets.remove(pos)
            # for move in aliens.movement:
            ## print(move.position.x)
            move = aliens.movement[i]
            print(move.fn)
            if move.fn != None:
                (vx, vy) = move.fn(t)
                print(vx, vy)
                move.position.x += dt * vx
                move.position.y += dt * vy
            else:
                move.position.x += dt * move.vx
                move.position.y += dt * move.vy

    def alienController(self, aliens, i, fn, t):
        aliens.movements[i].position.x += fn(t)

   
