import pygame
import c_components
import game
import copy

class RenderingSystem:
    def render(self, Movement, Sprite, Bullets):
        #Render bullets
        for pos in Bullets.bullets:
            pygame.draw.rect(game.SCREEN, "red", pygame.Rect(pos.x, pos.y, 5, 15))
        
        #Update & Render
        Sprite.update(Movement.position)
        game.SCREEN.blit(Sprite.image, Sprite.rect)