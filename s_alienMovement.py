import e_entity
import c_components

class AlienMovement:
    def moveAliensAndBullets(self, dt, aliens):
        for i in range(aliens.num):
            #Bullet Movement & deletion
            for pos in aliens.bullets[i].bullets:
                pos.y -= 25
                # Remove bullets that are off-screen
                if pos.y < -20:
                    aliens.bullets[i].bullets.remove(pos)
            print(aliens.movement)
            for move in aliens.movement:
                print(move.position.x)
                move.position.x += dt * move.vx
                move.position.y += dt * move.vy
            
