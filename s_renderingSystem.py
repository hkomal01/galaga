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
        health = ship_entity.health[0].health
        for i in range(min(health, 10)):
            hImage = pygame.transform.scale(ship_entity.sprite[0].image, 
                                            (ship_entity.sprite[0].image.get_width() 
                                             * 0.5, ship_entity.sprite[0].image.get_height()*0.5))
            hRect = hImage.get_rect()
            hRect.center = pygame.Vector2(40 + i * 50, 25)
            game.SCREEN.blit(hImage, hRect)
