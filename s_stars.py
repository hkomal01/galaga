import pygame
import c_components
import game
import copy
import random

class Stars:
    
    def createStar(self, star_entity):
        witdh = random.randrange(1, 4)
        height = witdh
        x = random.randrange(0, game.WIDTH) 
        y = -20
        vy = random.randrange(4, 25)
        movement = [x, y, 0, vy] #x, y, vx, vy
        star_entity.add_star([witdh, height], movement)
        
    def moveStar(self, dt, star_entity):
        for i, move in enumerate(star_entity.movement):
            move.position.x += dt * move.vx
            move.position.y += dt * move.vy
            