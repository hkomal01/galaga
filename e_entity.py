import pygame
import c_components as comp

class Ship:
    def __init__(self, hp, sprite, inputs, explosion, movement):
            self.health = [comp.Health(hp)]
            self.sprite = [comp.Sprite(sprite)]
            self.input_state = [comp.Input_State(inputs[0], inputs[1], inputs[2], inputs[3])]
            self.explosion = [comp.Explosion(explosion)]
            self.bullets = [comp.Bullets()]
            self.movement = [comp.Movement(movement[0], movement[1], movement[2], movement[3])]
class Alien:
    def __init__(self):
        self.health = []
        self.sprite = []
        self.movement = []
        self.explosion = []
        self.bullets =[]
        self.num = 0
    def add_alien(self, health, sprite, movement, explosion):
        self.health.append(comp.Health(health))
        self.sprite.append(comp.Sprite(sprite))
        self.movement.append(comp.Movement(movement[0], movement[1], movement[2], movement[3]))
        self.explosion.append(comp.Explosion(explosion))
        self.bullets.append(comp.Bullets())
        self.num += 1

    
