import pygame
import random
import game

class Health:
    def __init__(self, initHealth):
        self.health = initHealth

class Sprite:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width() 
                                             * 3, self.image.get_height()*3))
        self.rect = self.image.get_rect() # Retangular properties of the image

    def update(self, pos):
        self.rect.center = pos

class Input_State:
    def __init__(self, leftk, rightk, shootk, quitk, pausek):
        self.value = pygame.key.get_pressed()
        self.leftk = leftk
        self.rightk = rightk
        self.shootk = shootk
        self.quitk = quitk
        self.pausek = pausek
        self.update() #Leave it here

    def update(self):
        self.value = pygame.key.get_pressed()
        self.left = self.value[self.leftk]
        self.right = self.value[self.rightk]
        self.quit = self.value[self.quitk]
        self.pause = self.value[self.pausek]
        self.shoot = self.value[self.shootk]

class Movement:
    def __init__(self, x, y, vx, vy, fn = None, px = None, py = None):
        self.position = pygame.Vector2(x, y)
        self.vx = vx
        self.vy = vy
        self.t = 0
        self.fn = fn
        self.px = px
        self.py = py

class CoolDown:
    def __init__(self, cooldown_time):
        self.cooldownValue = cooldown_time
        self.cooldownTime = cooldown_time
        
class Size:
    def __init__(self, width, height):
        self.size = (width, height)
        
class Points:
    def __init__(self):
        self.points = 0
        
    def update(self):
        std_dev = (120 - 100) / 3
        num = round(random.gauss(100, std_dev))
        num = max(min(num, 120), 80)
        self.points += num