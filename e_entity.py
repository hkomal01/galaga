import pygame
import c_components as comp
import game
import math

class Ship:
	"""
	Represents a ship entity in the game.

	Attributes:
		health (list): A list containing a single `Health` component.
		sprite (list): A list containing a single `Sprite` component.
		input_state (list): A list containing a single `Input_State` component.
		movement (list): A list containing a single `Movement` component.
		cooldown (list): A list containing a single `CoolDown` component.
		points (list): A list containing a single `Points` component.
	"""

	def __init__(self, hp, sprite, inputs, movement, cooldown):
		self.health = [comp.Health(hp)]
		self.sprite = [comp.Sprite(sprite)]
		self.input_state = [comp.Input_State(inputs[0], inputs[1], 
											 inputs[2], inputs[3], 
											 inputs[4])]
		self.movement = [comp.Movement(movement[0], movement[1], 
									   movement[2], movement[3])]
		self.cooldown = [comp.CoolDown(cooldown)]
		self.points = [comp.Points()]

class Alien:
	"""
	Represents an alien entity in the game.
	
	Attributes:
		health (list): A list of Health objects representing the health of the alien.
		sprite (list): A list of Sprite objects representing the sprite of the alien.
		movement (list): A list of Movement objects representing the movement behavior of the alien.
		cooldown (list): A list of CoolDown objects representing the cooldown of the alien's bullets.
		num (int): The number of aliens created.
	"""
	def __init__(self):
		self.health = []
		self.sprite = []
		self.movement = []
		self.cooldown = []
		self.num = 0
		
	def add_alien(self, health, sprite, movement, cooldown, fn=None, px=None, py=None):
		"""
		Adds a new alien entity to the game.

		Parameters:
		- health (int): The initial health of the alien.
		- sprite (str): The sprite image file path for the alien.
		- movement (tuple): The movement parameters for the alien. It should be a tuple of four values:
			- movement[0] (float): The initial x-coordinate of the alien.
			- movement[1] (float): The initial y-coordinate of the alien.
			- movement[2] (float): The x-velocity of the alien.
			- movement[3] (float): The y-velocity of the alien.
		- cooldown (float): The cooldown time for the alien's actions.
		- fn (function, optional): A function to be called to determine alien's position.
		- px (float, optional): The x-coordinate of a target position for the alien's action.
		- py (float, optional): The y-coordinate of a target position for the alien's action.

		Returns:
		- None

		"""
		self.health.append(comp.Health(health))
		self.sprite.append(comp.Sprite(sprite))
		self.movement.append(comp.Movement(movement[0], movement[1], movement[2], movement[3], fn, px, py))
		self.cooldown.append(comp.CoolDown(cooldown))
		self.num += 1

class Explosion:
	"""
	Represents an explosion in the game.

	Attributes:
	- movement (list): A list of Movement objects representing the movement of the explosion.
	- animIndex (list): A list of integers representing the current animation index for each explosion.
	- sprites (list): A list of Sprite objects representing the sprites for the explosion animation.
	- num (int): The number of explosions.

	Methods:
	- add_explosion(movement): Adds a new explosion with the given movement parameters.
	"""

	def __init__(self):
		self.movement = []
		self.animIndex = []
		self.sprites = [
			comp.Sprite("sprites/explosion0.png"),
			comp.Sprite("sprites/explosion1.png"),
			comp.Sprite("sprites/explosion2.png"),
			comp.Sprite("sprites/explosion3.png"),
			comp.Sprite("sprites/explosion4.png"),
			comp.Sprite("sprites/explosion5.png"),
			comp.Sprite("sprites/explosion6.png")
		]
		self.num = 0

	def add_explosion(self, movement):
		"""
		Adds a new explosion with the given movement parameters.

		Parameters:
		- movement (list): A list of four integers representing the movement parameters (x, y, dx, dy).
		"""
		self.movement.append(comp.Movement(movement[0], movement[1], movement[2], movement[3]))
		self.animIndex.append(0)
		self.num += 1

class ShipBullet:
	"""
	Represents a bullet fired by the ship in the Galaga game.
	
	Attributes:
		movement (list): A list of `Movement` objects representing the bullet's movement.
	"""
	def __init__(self):
		self.movement = []
		
	def add_shipBullet(self, movement):
		"""
		Adds a `Movement` object to the `movement` list.
		
		Args:
			movement (list): A list containing the parameters for creating a `Movement` object.
				The parameters are: [start_x, start_y, speed_x, speed_y].
		"""
		self.movement.append(comp.Movement(movement[0], movement[1], 
										   movement[2], movement[3]))

class AlienBullet:
		"""
		Represents a bullet fired by an alien in the Galaga game.
		"""

		def __init__(self):
				self.movement = []

		def add_alienBullet(self, movement):
				"""
				Adds a movement to the alien bullet.

				Parameters:
				- movement (list): A list containing the movement parameters for the bullet.
					The list should have the following format: [start_x, start_y, speed_x, speed_y]
				"""
				self.movement.append(comp.Movement(movement[0], movement[1], movement[2], movement[3]))
		
class Star:
	"""
	Represents a star in the game Galaga.
	
	Attributes:
		size (list): A list containing the size of the star in pixels.
		movement (list): A list containing the movement parameters of the star.
	"""
	def __init__(self):
		self.size = []
		self.movement = []
		
	def add_star(self, size, movement):
		"""
		Adds a star to the star list with the given size and movement parameters.
		
		Args:
			size (tuple): A tuple containing the width and height of the star in pixels.
			movement (tuple): A tuple containing the x and y velocities, and the x and y accelerations of the star.
		"""
		self.size.append(comp.Size(size[0], size[1]))
		self.movement.append(comp.Movement(movement[0], movement[1], 
										   movement[2], movement[3]))
		
		
