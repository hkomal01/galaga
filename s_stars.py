import game
import random

class Stars:
    """
    Represents a collection of stars in a sky.
    """

    def initiateSky(self, star_entity):
        """
        Initializes the sky with a random set of stars.

        Args:
            star_entity: The entity representing the stars in the game.
        """
        for _ in range(0, 300):
            width = random.randrange(1, 4)
            height = width
            x = random.randrange(0, game.WIDTH) 
            y = random.randrange(0, game.HEIGHT) 
            vy = random.randrange(130, 150)
            movement = [x, y, 0, vy] #x, y, vx, vy
            star_entity.add_star([width, height], movement)
    
    def createStar(self, star_entity):
        """
        Creates a single star at the top of the screen.

        Args:
            star_entity: The entity representing the stars in the game.
        """
        width = random.randrange(1, 4)
        height = width
        x = random.randrange(0, game.WIDTH) 
        y = -20
        vy = random.randrange(130, 150)
        movement = [x, y, 0, vy] #x, y, vx, vy
        star_entity.add_star([width, height], movement)
        
    def moveStar(self, dt, star_entity):
        """
        Moves the stars downwards based on the elapsed time.

        Args:
            dt: The elapsed time since the last frame.
            star_entity: The entity representing the stars in the game.
        """
        starsForDeletion = []
        
        for i, move in enumerate(star_entity.movement):
            move.position.x += dt * move.vx
            move.position.y += dt * move.vy
            if move.position.y > game.HEIGHT:
                starsForDeletion.append(i)
            
        for p in starsForDeletion[::-1]:
            del star_entity.movement[p]
            del star_entity.size[p]
            