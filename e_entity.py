import pygame
import c_components

class Ship:
    def __init__(self):
        self.health = []
        self.sprite = []
        self.input_state = []
        self.movement = []
        self.explosion = []
        
    def addSprite(self, c_sprite):
        self.sprite.append(c_sprite)