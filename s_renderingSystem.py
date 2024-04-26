import pygame
import game

class RenderingSystem:
    """
    A class that handles rendering in the game.

    Methods:
    - render: Updates and renders the game sprites.
    - renderBullets: Renders the ship and alien bullets.
    - renderHud: Renders the health bar.
    - renderText: Renders text on the screen.
    - renderStar: Renders stars on the screen.
    """

    def render(self, Movement, Sprite):
        """
        Updates and renders the game sprites.

        Parameters:
        - Movement: The movement component of the sprite.
        - Sprite: The sprite component to be rendered.
        """
        # Update & Render
        Sprite.update(Movement.position)
        game.SCREEN.blit(Sprite.image, Sprite.rect)
        
    def renderBullets(self, shipBullet_entity, alienBullet_entity):
        """
        Renders the ship and alien bullets.

        Parameters:
        - shipBullet_entity: The entity containing ship bullets.
        - alienBullet_entity: The entity containing alien bullets.
        """
        for mov in shipBullet_entity.movement:
            pygame.draw.rect(game.SCREEN, "red", pygame.Rect(mov.position.x, mov.position.y, 5, 15))
        for mov in alienBullet_entity.movement:
            pygame.draw.rect(game.SCREEN, "red", pygame.Rect(mov.position.x, mov.position.y, 5, 15))

    def renderHud(self, ship_entity):
        """
        Renders the health bar.

        Parameters:
        - ship_entity: The entity containing the ship.
        """
        # Render health
        health = ship_entity.health[0].health
        for i in range(min(health, 10)):
            hImage = pygame.transform.scale(ship_entity.sprite[0].image, 
                                            (ship_entity.sprite[0].image.get_width() 
                                             * 0.5, ship_entity.sprite[0].image.get_height()*0.5))
            hRect = hImage.get_rect()
            hRect.center = pygame.Vector2(40 + i * 50, 25)
            game.SCREEN.blit(hImage, hRect)
            
    def renderText(self, message, color, xPos, yPos):
        """
        Renders text on the screen.

        Parameters:
        - message: The text message to be rendered.
        - color: The color of the text.
        - xPos: The x-coordinate position of the text.
        - yPos: The y-coordinate position of the text.
        """
        font = pygame.font.SysFont("Press Start 2P", 50)
        goImage = font.render(message, 0, color)
        goRect = goImage.get_rect()
        goRect.x = xPos // 2 - goRect.width // 2
        goRect.y = yPos // 2 - goRect.height // 2
        game.SCREEN.blit(goImage, goRect)
        return

    def renderStar(self, start_entity):
        """
        Renders stars on the screen.

        Parameters:
        - start_entity: The entity containing the stars.
        """
        color = (255, 255, 255)
        for (starSize, starMovement) in zip(start_entity.size, start_entity.movement):
            sImage = pygame.Surface(starSize.size)
            sImage.fill(color)
            sRect = sImage.get_rect()
            sRect.x = starMovement.position.x
            sRect.y = starMovement.position.y
            game.SCREEN.blit(sImage, sRect)
