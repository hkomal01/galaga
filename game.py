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
import time
import threading
import math

def sinMovement(t):
	if t > 100 and t < 200:
		return (0, 0)
	return (500 * math.sin(t * .1), 30)

def move2(t):
	return (1000 * math.sin(t), 30)

def circleMovement(t):
	if t > 100 and t < 200:
		return (0, 0)
	return (50 * math.sin(t * .1), 30)

# Constant rotation time (period and radius parameterized by rot time)
def enter(t):
	# Rotation completes every 100 frames
	period = 2 * math.pi / 100
	r = 768
	if (math.isclose(math.cos(period * t), 0, rel_tol=.99)):
		print(r * math.cos(period * t))
	return (r * math.cos(period * (t)), r * math.sin(period * (t)))

# Constant radius. 
def enter2(t):
	r = 334
	w = (2 * math.pi) / 100

	return (r * math.cos(w * t), r * math.sin(w * t))


WIDTH = 1024
HEIGHT = 768
SHIPBASEHEALTH = 101010
SHIP_SPRITE = "sprites/ship.png"
KEYS = [pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_ESCAPE, pygame.K_p]
MOVEMENT = [WIDTH / 2, (HEIGHT / 6) *5, 300, 0]
COOLDOWN = 0.18
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
pygame.font.init()

running = True
dt = 0

if __name__ == "__main__":
	
	pygame.init()
	
	#ENTITIES
	ship_entity = e_entity.Ship(SHIPBASEHEALTH, SHIP_SPRITE, KEYS, MOVEMENT, 
								COOLDOWN)
	shipBullet_entity = e_entity.ShipBullet()
	
	aliens_entities = e_entity.Alien()
	# aliens_entities.add_alien(1, "sprites/enemy1.png", 
	# 					     (1 * WIDTH / 6, HEIGHT / 2, 0, -0), 1)
	# aliens_entities.add_alien(1, "sprites/enemy2.png", 
	# 					     (2 * WIDTH / 6, HEIGHT / 2, 0, 0), 1.5)
	# aliens_entities.add_alien(1, "sprites/enemy3.png", 
	# 					     (2.5 * WIDTH / 6, HEIGHT/2, 0, 0), .5)
	aliens_entities.add_alien(1, "sprites/enemy2.png", 
							 (1 * WIDTH / 4, (HEIGHT / 6) * 5 - 10, 0, 0), 3)
	aliens_entities.add_alien(1, "sprites/enemy3.png", 
							 (WIDTH / 2, 0, 0, 0), 3, enter2)
	aliens_entities.add_alien(1, "sprites/enemy1.png", 
							 (4 * WIDTH / 6, HEIGHT - 600, 0, 0), .5, sinMovement)

	# aliens_entities.add_alien(1, "sprites/enemy2.png", 
	#  						 (5 * WIDTH / 6, HEIGHT / 2, 1, -1), 2, circleMovement)
	alienBullet_entity = e_entity.AlienBullet()
	
	explosion_entities = e_entity.Explosion()
	
	#SYSTEMS
	ship_system = s_shipMovement.ShipMovement()
	aliens_system = s_alienMovement.AlienMovement()
	rendering_system = s_renderingSystem.RenderingSystem()
	collision_system = s_collisionDetection.CollisionSystem()
	explosion_system = s_explosion.ExplosionSystem()
	frame_count = -1

	while running and not ship_entity.input_state[0].quit:
		frame_count += 1
		if frame_count == 100:
			aliens_entities.add_alien(1, "sprites/enemy3.png", 
							 (WIDTH / 2 - 100, 0, 0, 0), 3/4, enter2)
		if frame_count == 200:
			aliens_entities.add_alien(1, "sprites/enemy3.png", 
							 (WIDTH / 2 + 100, 0, 0, 0), 3/4, enter2)
		if frame_count == 300:
			aliens_entities.add_alien(1, "sprites/enemy3.png", 
							 (WIDTH / 2 - 200, 0, 0, 0), 3/4, enter2)
		if frame_count == 400:
			aliens_entities.add_alien(1, "sprites/enemy3.png", 
							 (WIDTH / 2 + 200, 0, 0, 0), 3/4, enter2)

		# poll for events
		# pygame.QUIT event means the user clicked X to close your window
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		# fill the screen with a color to wipe away anything from last frame
		SCREEN.fill("black")

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
  
		for thread in threads:
			thread.start()
		for thread in threads:
			thread.join()

		#SYSTEM
		#COLLISION THREADS
		threads2 = []
		
		if frame_count > 2:	
			threads2.append(threading.Thread(target=
									collision_system.checkShipAlienCollision,
											args = (aliens_entities,
														explosion_entities, 
														ship_entity)))
		threads2.append(threading.Thread(target=
								   collision_system.checkAlienCollision,
										args = (shipBullet_entity, 
													aliens_entities, 
													explosion_entities)))
		threads2.append(threading.Thread(target=
								   collision_system.checkShipCollision,
										args = (alienBullet_entity,
													explosion_entities, 
													ship_entity)))
		for thread in threads2:
			thread.start()
		for thread in threads2:
			thread.join()
  
		#SYSTEM
		#RENDERING THREADS
		threads3 = []
		
		if ship_entity.health[0].health > 0:
			threads3.append(threading.Thread(target=rendering_system.render,
		  						args = (ship_entity.movement[0], 
				 						ship_entity.sprite[0])))
		else:
			threads3.append(threading.Thread(target=rendering_system.renderText,
								args = ("GAME OVER", (255, 0, 0), WIDTH, HEIGHT)))
		
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
		threads3.append(threading.Thread(target=rendering_system.renderHud,
								args = (ship_entity,)))

		for thread in threads3:
			thread.start()
		for thread in threads3:
			thread.join()

		# flip() the display to put your work on screen
		pygame.display.flip()
			
		# limits FPS to 60
		# dt is delta time in seconds since last frame, used for framerate-
		# independent physics.
		dt = clock.tick(60) / 1000

	pygame.quit()