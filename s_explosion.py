class ExplosionSystem:
    """
    A class that represents the explosion system in the game.
    
    Attributes:
        None
        
    Methods:
        update(explosion_entity): Updates the explosion animation for the given explosion entity.
    """
    
    def update(self, explosion_entity):
        """
        Updates the explosion animation for the given explosion entity.
        
        Args:
            explosion_entity (ExplosionEntity): The explosion entity to update.
            
        Returns:
            None
        """
        for i in range(len(explosion_entity.animIndex) - 1, -1, -1):
            explosion_entity.animIndex[i] += 1
            if explosion_entity.animIndex[i] == 7:
                del explosion_entity.movement[i]
                del explosion_entity.animIndex[i]
                explosion_entity.num -= 1
