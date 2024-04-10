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