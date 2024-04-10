import pygame
import c_components as comp
import game
class Ship:
    def __init__(self, hp, sprite, inputs, movement, cooldown):
            self.health = [comp.Health(hp)]
            self.sprite = [comp.Sprite(sprite)]
            self.input_state = [comp.Input_State(inputs[0], inputs[1], 
                                                 inputs[2], inputs[3], inputs[4])]
            self.movement = [comp.Movement(movement[0], movement[1], 
                                           movement[2], movement[3])]
            self.cooldown = [comp.CoolDown(cooldown)]

class Alien:
    def __init__(self):
        self.health = []
        self.sprite = []
        self.movement = []
        self.cooldown = []
        self.num = 0
        
    def add_alien(self, health, sprite, movement, cooldown):
        self.health.append(comp.Health(health))
        self.sprite.append(comp.Sprite(sprite))
        self.movement.append(comp.Movement(movement[0], movement[1], 
                                           movement[2], movement[3]))
        self.cooldown.append(comp.CoolDown(cooldown))
        self.num += 1

class Explosion:
    def __init__(self):
        self.movement = []
        self.animIndex = []
        self.sprites = \
            [comp.Sprite("sprites/explosion0.png"),
            comp.Sprite("sprites/explosion1.png"),
            comp.Sprite("sprites/explosion2.png"),
            comp.Sprite("sprites/explosion3.png"),
            comp.Sprite("sprites/explosion4.png"),
            comp.Sprite("sprites/explosion5.png"),
            comp.Sprite("sprites/explosion6.png")]
        self.num = 0

    def add_explosion(self, movement):
        self.movement.append(comp.Movement(movement[0], movement[1], 
                                           movement[2], movement[3]))
        self.animIndex.append(0)
        self.num += 1

class ShipBullet:
    def __init__(self):
        self.movement = []
        
    def add_shipBullet(self, movement):
        self.movement.append(comp.Movement(movement[0], movement[1], 
                                           movement[2], movement[3]))

class AlienBullet:
    def __init__(self):
        self.movement = []
    def add_alienBullet(self, movement):
        self.movement.append(comp.Movement(movement[0], movement[1], 
                                           movement[2], movement[3]))
        
