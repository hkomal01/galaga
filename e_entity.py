import pygame
import c_components as comp

class Ship:
    def __init__(self, hp, sprite, inputs, explosion):
            self.health = [comp.Health(hp)]
            self.sprite = [comp.Sprite(sprite)]
            self.input_state = [comp.Input_State(inputs[0], inputs[1], inputs[2], inputs[3])]
            self.explosion = [comp.Explosion(explosion)]
            self.bullets = [comp.Bullets()]
class Alien:
    def __init__(self,):
        self.health = []
        self.sprite = []
        self.movement = []
        self.explosion = []
    def add_alien(self, health, sprite, movement, explosion):
        self.health.append(comp.Health(health))
        self.sprite.append(comp.Sprite(sprite))
        self.movement.append(comp.Movement(movement))
        self.explosion.append(comp.explosion(explosion))
    
