import e_entity
import c_components

class ExplosionSystem:            
    def update(self, explosion_entity):
        for i in range(len(explosion_entity.animIndex) - 1, -1, -1):
            explosion_entity.animIndex[i] += 1
            if (explosion_entity.animIndex[i] == 7):
                del explosion_entity.movement[i]
                del explosion_entity.animIndex[i]
                explosion_entity.num -= 1
