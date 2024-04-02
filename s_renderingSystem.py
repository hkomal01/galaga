import pygame
import c_components
import game
import copy

class RenderingSystem:
    def render(self, InputState, Sprite, Bullets):
        #Update & Render ship
        Sprite.update(InputState.player_pos)
        game.SCREEN.blit(Sprite.image, Sprite.rect)

        for pos in Bullets.bullets:
            pygame.draw.rect(game.SCREEN, "red", pygame.Rect(pos.x, pos.y, 5, 15))
            pos.y -= 25
            # Remove bullets that are off-screen
            if pos.y < -20:
                Bullets.bullets.remove(pos)
        