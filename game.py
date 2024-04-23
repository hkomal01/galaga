import pygame
import numpy as np
import copy
import c_components
import e_entity
import s_shipMovement
import s_alienMovement
import s_renderingSystem
import s_collisionDetection
import s_explosion
import s_stars
import time
import threading
import math

WIDTH = 768 #1024
HEIGHT = 1024 #768
SHIPBASEHEALTH = 125
SHIP_SPRITE = "sprites/ship.png"
SOUNDTRACK = "sounds/soundtrack8bit.mp3"
KEYS = [pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_ESCAPE, pygame.K_p]
MOVEMENT = [WIDTH / 2, (HEIGHT / 6) *5, 450, 0]
COOLDOWN = 0.3
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FRAMEEND = 3600

def enter(move):
	t = move.t
	y = 20*t
	sign = move.px
	x = (sign * 300 * math.sin(t * (1 / (2 * math.pi))) + move.vx)
	if y >= move.vy:
		move.fn = stay
		return stay(move)
	return (x, y, 5)

def stay(move):
	return (move.position.x, move.position.y, 0)

def enter_rev(move):
	t = move.t
	amplitude = 300 # Increase this for higher amplitude
	frequency = 1 / (2 * math.pi)  # Decrease this for lower frequency
	# if t > 10:
	# 	return (amplitude * math.sin(t * frequency), amplitude * math.cos(t * frequency), .5)
	# else:
	if 20*t < (200):
		move.fn = enter
		return enter(move)
	return (amplitude * math.sin(t * frequency) + 354, 20*t, -5)

def cornerguy(move):
	t = move.t
	return (WIDTH - move.vx, 50 * math.sin(t) + 100, 1)

def sintoside(move):
	t = move.t
	x = 200 * math.sin((t) * (1 / (2 * math.pi) )) + 450
	y = 20*t
	if y > (HEIGHT - 500):
		move.fn = side
		move.px = x
		move.py = y
		move.t = math.asin((x - 354) / 300) 
		return (x, y, 1)
	return (x, y, 7)

def side(move):
	t = move.t
	x = 300 * math.sin(t) + 354
	y = move.py
	return (x, y, 1)

def sin(move):
	t = move.t
	x = 200 * math.sin((t) * (1 / (2 * math.pi) )) + 250
	y = 20*t
	return (x, y, 7)

def sin1(move):
	t = move.t
	x = 200 * math.sin((t) * (1 / (2 * math.pi) )) + 354
	y = 20*t
	if y > (HEIGHT - 600):
		move.fn = sidetoside
		move.px = x
		move.py = y
		move.t = math.asin((x - 354) / 300) 
		return (x, y, 1)
	return (x, y, 7)

def infinity(move):
	if move.t == 0:
		move.t = move.px
	t = move.t
	x = 200 * (math.sin(t) / (1 + math.cos(t)**2)) + 400
	y = 150 * (math.cos(t)*math.sin(t) / (1 + math.cos(t)**2)) + 100
	return (x, y, 3)

def sidetoside(move):
	t = move.t
	x = 300 * math.sin(t) + 354
	y = move.py
	if np.isclose(x, move.px, .01):
		move.fn = sin2
		move.py = y
		move.px = x
		# move.t = math.asin((x - 354) / 300)
		move.t = math.asin((x - 354) / 300) / (1 / (2 * math.pi))
		return (x, y, 1)
	return (x, y, 1)

def sin2(move):
	t = move.t
	x = 300 * math.sin((t) * (1 / (2 * math.pi) )) + 354
	y = 20*(t + 1.5) + move.py
	return (x, y, 7)

def pause(clock, rendering_system):
	global running
	pause = True
 
	#Render Pause message`
	rendering_system.renderText("PAUSED", (255, 255, 255), WIDTH, HEIGHT)
	pygame.display.flip()
 
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_p:
					pause = False
				if event.key == pygame.K_ESCAPE:
					pause = False
					running = False
			if event.type == pygame.QUIT:
				pause = False
				running = False
				
	clock.tick()
 
def endGame(aliens_entities, explosion_entities):
    for i in range(aliens_entities.num-1, -1, -1):
                movement = aliens_entities.movement[i]
                explosion_entities.add_explosion((movement.position.x, movement.position.y, 0, 0))
                del aliens_entities.health[i]
                del aliens_entities.sprite[i]
                del aliens_entities.movement[i]
                del aliens_entities.cooldown[i]
                aliens_entities.num -= 1           
    
    return
	
def main():
    #Initiate variables
	clock = pygame.time.Clock()
	pygame.font.init()

	running = True
	dt = 0

	alienLock = threading.Lock()
	pygame.init()
	
	#ENTITIES
	ship_entity = e_entity.Ship(SHIPBASEHEALTH, SHIP_SPRITE, KEYS, MOVEMENT, 
								COOLDOWN)
	shipBullet_entity = e_entity.ShipBullet()
	
	aliens_entities = e_entity.Alien()

	alienBullet_entity = e_entity.AlienBullet()
	
	explosion_entities = e_entity.Explosion()
 
	star_entities = e_entity.Star()
	
	#SYSTEMS
	ship_system = s_shipMovement.ShipMovement()
	aliens_system = s_alienMovement.AlienMovement()
	rendering_system = s_renderingSystem.RenderingSystem()
	collision_system = s_collisionDetection.CollisionSystem()
	explosion_system = s_explosion.ExplosionSystem()
	star_system = s_stars.Stars()
	frame_count = -1
 
	#Soundtrack initialization
	pygame.mixer.init()
	pygame.mixer.music.load(SOUNDTRACK)
	pygame.mixer.music.set_volume(0.7)
	pygame.mixer.music.play(loops=-1)
	mute = False
 
	#Initialize background 
	star_system.initiateSky(star_entities)
	right = True
	swap = True
	i = 0



	while running and not ship_entity.input_state[0].quit:
		frame_count += 1 
		
		if ship_entity.health[0].health > 0:
			#End game (Explode aliens)
			if frame_count >= FRAMEEND:
				endGame(aliens_entities, explosion_entities)
	
			#Spawn aliens
			else:
				if frame_count < 500:
					if frame_count % 200 == 0:
						if right:
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(300, 0, 300, (frame_count/200 * 100) + 300), 2, enter, px=1)				
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(400, 0, 400, (frame_count/200 * 100) + 300), 1.5, enter, px=1)
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(200, 0, 500, (frame_count/200 * 100) + 300), 1.75, enter, px=1)
							right = False
						else: 
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(300, 0, 300, (frame_count/200 * 100) + 300), 2, enter, px=-1)				
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(400, 0, 400, (frame_count/200 * 100) + 300), 1.5, enter, px=-1)
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(200, 0, 500, (frame_count/200 * 100) + 300), 1.75, enter, px=-1)
							right = True
				if frame_count > 600:
					if swap:
						if frame_count % 600 == 20 or frame_count % 600 == 40 or frame_count % 600 == 60 and swap:
							aliens_entities.add_alien(1, "sprites/enemy1.png", 
											( WIDTH / 2, 0, 0, 0), 1.5, sin1)
						if frame_count % 600 == 20 or frame_count % 600 == 40 or frame_count % 600 == 60 and swap:
							aliens_entities.add_alien(1, "sprites/enemy1.png", 
											( WIDTH / 4, 0, 0, 0), 1.5, sin)
						if frame_count % 600 == 20 or frame_count % 600 == 40 or frame_count % 600 == 60 and swap:
							aliens_entities.add_alien(1, "sprites/enemy2.png", 
											( WIDTH / 2, 0, 0, 0), 1.5, sintoside)
						if frame_count % 600 == 0:
							swap = False
					elif frame_count % 200 == 0 and not swap:
						if right:
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(0, 0, 300, 300 - i), 2, enter, px=1)				
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(0, 0, 400, 300 - i), 1.5, enter, px=1)
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(0, 0, 500, 300 - i), 1.75, enter, px=1)
							right = False
						else: 
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(0, 0, 300, 300 - i), 2, enter, px=-1)				
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(0, 0, 400, 300 - i), 1.5, enter, px=-1)
							aliens_entities.add_alien(1, "sprites/enemy3.png", 
										(0, 0, 500, 300 - i), 1.75, enter, px=-1)
							right = True
						if frame_count % 600 == 0 and not swap:
							i += 50
							swap = True
				#Starters
				if frame_count == 0:
					aliens_entities.add_alien(1, "sprites/enemy1.png", 
									( WIDTH / 2, 0, 0, 0), .5, infinity, px=2 * math.pi/3)
					aliens_entities.add_alien(1, "sprites/enemy2.png", 
									( WIDTH / 2, 0, 0, 0), .75, infinity, px= 4 * math.pi/3)
					aliens_entities.add_alien(1, "sprites/enemy3.png", 
									( WIDTH / 2, 0, 0, 0), 1, infinity, px=0)
					aliens_entities.add_alien(1, "sprites/enemy3.png", 
									( WIDTH / 2, 0, 35, 0), 1, cornerguy)
					aliens_entities.add_alien(1, "sprites/enemy3.png", 
									( WIDTH / 2, 0, WIDTH - 35, 0), 1, cornerguy)
		
		

		#Poll for events QUIT, MUTE, and PAUSE
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_m:
					if mute:
						mute = False
						pygame.mixer.music.unpause()
					else:
						mute = True
						pygame.mixer.music.pause()
				if event.key == pygame.K_p and ship_entity.health[0].health > 0 and frame_count < FRAMEEND:					
					pause(clock, rendering_system)
				if event.key == pygame.K_r and (frame_count >= FRAMEEND or ship_entity.health[0].health <= 0):
					return True
		
		#SYSTEM
		#MOVEMENT & EXPLOSION THREADS
		threads = []

		threads.append(threading.Thread(target=ship_system.moveShip,
							args = (dt, ship_entity, shipBullet_entity)))
		threads.append(threading.Thread(target=ship_system.moveShipBullets,
							args = (dt, shipBullet_entity)))
		threads.append(threading.Thread(target=aliens_system.moveAliens,
							args = (dt, aliens_entities, alienBullet_entity, frame_count)))
		threads.append(threading.Thread(target=aliens_system.moveAlienBullets,
							args = (dt, alienBullet_entity)))
		threads.append(threading.Thread(target=explosion_system.update,
		 					args = (explosion_entities,)))
		threads.append(threading.Thread(target=star_system.moveStar,
		 					args = (dt, star_entities)))
  
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()

		#SYSTEM
		#COLLISION & STAR CREATION THREADS
		threads2 = []
		
		if frame_count > 2:	
			threads2.append(threading.Thread(target=
									collision_system.checkShipAlienCollision,
											args = (aliens_entities,
														explosion_entities, 
														ship_entity,
			  											alienLock)))
		threads2.append(threading.Thread(target=
								   collision_system.checkAlienCollision,
										args = (ship_entity,
                  									shipBullet_entity, 
													aliens_entities, 
													explosion_entities,
			 										alienLock)))
		threads2.append(threading.Thread(target=
								   collision_system.checkShipCollision,
										args = (alienBullet_entity,
													explosion_entities, 
													ship_entity)))
		threads2.append(threading.Thread(target= star_system.createStar,
										args = (star_entities,)))

		for thread in threads2:
			thread.start()
		for thread in threads2:
			thread.join()
  
		#SYSTEM
		#RENDERING THREADS
  
		#Render background
		SCREEN.fill("black")
		rendering_system.renderStar(star_entities)

		threads3 = []
		
		if ship_entity.health[0].health > 0:
			threads3.append(threading.Thread(target=rendering_system.render,
		  						args = (ship_entity.movement[0], 
				 						ship_entity.sprite[0])))
		
		for i in range(aliens_entities.num):
			threads3.append(threading.Thread(target=rendering_system.render,
		  						args = (aliens_entities.movement[i],
										aliens_entities.sprite[i])))
		for n in range(explosion_entities.num):
			threads3.append(threading.Thread(target=rendering_system.render,
		  						args = (explosion_entities.movement[n], 
										explosion_entities.sprites
										[explosion_entities.animIndex[n]])))
		threads3.append(threading.Thread(target=rendering_system.renderBullets,
								args = (shipBullet_entity, alienBullet_entity)))

		for thread in threads3:
			thread.start()
		for thread in threads3:
			thread.join()

		#Render HUD
		rendering_system.renderHud(ship_entity)
		points = ship_entity.points[0].points
		health = ship_entity.health[0].health
		if frame_count >= FRAMEEND and health > 0:
			points += 2000 + (health * 500)
			rendering_system.renderText(f"UNIVERSE SAVED", 
 									(255, 255, 0), WIDTH, HEIGHT * 0.9)
			rendering_system.renderText(f"+2000 pts - Saved Universe", 
 									(255, 255, 0), WIDTH, HEIGHT)
			if health == 1:
				rendering_system.renderText(f"+{health * 500} pts - 1 life left", 
 									(255, 255, 0), WIDTH, HEIGHT * 1.1)
			else:
				rendering_system.renderText(f"+{health * 500} pts - {health} lives left", 
 									(255, 255, 0), WIDTH, HEIGHT * 1.1)
			rendering_system.renderText(f"Points: {points}", 
 									(255, 255, 255), WIDTH, HEIGHT * 1.2)
		else:
			rendering_system.renderText(f"Points: {points}", 
 									(255, 255, 255), WIDTH * 1.7, HEIGHT * 0.07)
   
		if ship_entity.health[0].health <= 0:
			rendering_system.renderText("GAME OVER", (255, 0, 0), WIDTH, HEIGHT)

		# flip() the display to put your work on screen
		pygame.display.flip()
			
		# limits FPS to 60
		# dt is delta time in seconds since last frame, used for framerate-
		# independent physics.
		dt = clock.tick(60) / 1000

	return False

if __name__ == "__main__":
	gameState = True
	while gameState:
 		gameState = main()