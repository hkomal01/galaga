import pygame
import c_components
import game
import copy

class RenderingSystem:
    def render(self, Movement, Sprite):
        #Update & Render
        Sprite.update(Movement.position)
        game.SCREEN.blit(Sprite.image, Sprite.rect)
        
    def renderBullets(self, shipBullet_entity, alienBullet_entity):
        for mov in shipBullet_entity.movement:
            pygame.draw.rect(game.SCREEN, "red", pygame.Rect(mov.position.x, mov.position.y, 5, 15))
        for mov in alienBullet_entity.movement:
            pygame.draw.rect(game.SCREEN, "red", pygame.Rect(mov.position.x, mov.position.y, 5, 15))

    def renderHud(self, ship_entity):
        #Render health
        health = ship_entity.health[0].health
        for i in range(min(health, 10)):
            hImage = pygame.transform.scale(ship_entity.sprite[0].image, 
                                            (ship_entity.sprite[0].image.get_width() 
                                             * 0.5, ship_entity.sprite[0].image.get_height()*0.5))
            hRect = hImage.get_rect()
            hRect.center = pygame.Vector2(40 + i * 50, 25)
            game.SCREEN.blit(hImage, hRect)
            
    def renderText(self, message, color, xPos, yPos):
        font = pygame.font.SysFont("Press Start 2P", 50)
        goImage = font.render(message, 0, color)
        goRect = goImage.get_rect()
        goRect.x = xPos // 2 - goRect.width // 2
        goRect.y = yPos // 2 - goRect.height // 2
        game.SCREEN.blit(goImage, goRect)
        return

    def renderStar(self, start_entity):
        color = (255, 255, 255)
        for (starSize, starMovement) in zip(start_entity.size, start_entity.movement):
            sImage = pygame.Surface(starSize.size)
            sImage.fill(color)
            sRect = sImage.get_rect()
            sRect.x = starMovement.position.x
            sRect.y = starMovement.position.y
            game.SCREEN.blit(sImage, sRect)
