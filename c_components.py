import pygame
import game
class Health:
    def __init__(self, initHealth):
        self.health = initHealth
        

class Sprite:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 3, self.image.get_height()*3))
        self.rect = self.image.get_rect() #Retangular properties of the image

    def update(self, pos):
        self.rect.center = pos

class Input_State:
    def __init__(self, leftk, rightk, shootk, quitk):
        self.value = pygame.key.get_pressed()
        self.leftk = leftk
        self.rightk = rightk
        self.shootk = shootk
        self.quitk = quitk
        self.player_pos = pygame.Vector2(game.WIDTH / 2, (game.HEIGHT / 6) *5)
        self.cooldown = 0
        self.cooldown_time = .18
        self.update()

    def update(self):
        self.value = pygame.key.get_pressed()
        self.left = self.value[self.leftk]
        self.right = self.value[self.rightk]
        self.quit = self.value[self.quitk]
        self.escape = False
        self.shoot = self.value[self.shootk]

class Movement:
    def __init__(self, x, y, velocity):
        self.x = x
        self.y = y
        self.velocity = velocity

class Explosion:
    def __init__(self, image):
        self.image = image
        self.is_dead = False

class Bullets:
    def __init__(self):
        self.bullets = []