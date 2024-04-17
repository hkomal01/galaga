import pygame
import c_components
import game
import copy
import random

class Stars:
    
    def initiateSky(self, star_entity):
        for i in range(0, 300):
            width = random.randrange(1, 4)
            height = width
            x = random.randrange(0, game.WIDTH) 
            y = random.randrange(0, game.HEIGHT) 
            vy = random.randrange(130, 150)
            movement = [x, y, 0, vy] #x, y, vx, vy
            star_entity.add_star([width, height], movement)
    
    def createStar(self, star_entity):
        width = random.randrange(1, 4)
        height = width
        x = random.randrange(0, game.WIDTH) 
        y = -20
        vy = random.randrange(130, 150)
        movement = [x, y, 0, vy] #x, y, vx, vy
        star_entity.add_star([width, height], movement)
        
    def moveStar(self, dt, star_entity):
        starsForDeletion = []
        
        for i, move in enumerate(star_entity.movement):
            move.position.x += dt * move.vx
            move.position.y += dt * move.vy
            if move.position.y > game.HEIGHT:
                starsForDeletion.append(i)
            
        for p in starsForDeletion[::-1]:
            del star_entity.movement[p]
            del star_entity.size[p]
            