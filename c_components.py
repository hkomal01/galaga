import pygame
import random

class Health:
    """
    Hold the health for each entity in game

    Attributes:
        health (int): Initial health for entity
    """
    def __init__(self, initHealth):
        self.health = initHealth

class Sprite:
    """
    Represents a sprite object in the game.

    Attributes:
        image (pygame.Surface): The image of the sprite.
        rect (pygame.Rect): The rectangular properties of the image.

    Methods:
        update(self, pos): Updates the position of the sprite.
    """

    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, 
                                            (self.image.get_width() 
                                             * 3, self.image.get_height()*3))
        self.rect = self.image.get_rect()

    def update(self, pos):
        """
        Updates the position of the sprite.

        Args:
            pos (tuple): The new position of the sprite as a tuple (x, y).
        """
        self.rect.center = pos

class Input_State:
    """
    Represents the state of the input for the game.

    Attributes:
        leftk (int): The key code for the left movement key.
        rightk (int): The key code for the right movement key.
        shootk (int): The key code for the shoot key.
        quitk (int): The key code for the quit key.
        pausek (int): The key code for the pause key.
        value (tuple): A tuple representing the current state of all keys.
        left (bool): True if the left movement key is pressed, False otherwise.
        right (bool): True if the right movement key is pressed, False otherwise.
        quit (bool): True if the quit key is pressed, False otherwise.
        pause (bool): True if the pause key is pressed, False otherwise.
        shoot (bool): True if the shoot key is pressed, False otherwise.
    """

    def __init__(self, leftk, rightk, shootk, quitk, pausek):
        self.value = pygame.key.get_pressed()
        self.leftk = leftk
        self.rightk = rightk
        self.shootk = shootk
        self.quitk = quitk
        self.pausek = pausek
        self.update() #Leave it here

    def update(self):
        """
        Updates the state of the input based on the current key presses.
        """
        self.value = pygame.key.get_pressed()
        self.left = self.value[self.leftk]
        self.right = self.value[self.rightk]
        self.quit = self.value[self.quitk]
        self.pause = self.value[self.pausek]
        self.shoot = self.value[self.shootk]

class Movement:
    """
    Hold movement related state for entities

    Attributes:
        position (int, int): Tuple which holds the coordinates for the entity
        vx (float): Holds constant horizontal velocity
        vy (float): Holds constant vertical velocity
        t (float): Parameter to be passed to the movement function
        fn (float -> (float, float, float)): Function which determines the 
            position of the entity and returns (x-coord, y-coord, t increment)
        px (float): Holds a x-coordinate to be referred back to
        px (float): Holds a y-coordinate to be referred back to
    """
    def __init__(self, x, y, vx, vy, fn = None, px = None, py = None):
        self.position = pygame.Vector2(x, y)
        self.vx = vx
        self.vy = vy
        self.t = 0
        self.fn = fn
        self.px = px
        self.py = py

class CoolDown:
    """
    Holds bullet cooldown for shooting entities

    Attributes:
        cooldownValue (float): Stores how long it has been since last bullet
        cooldownTime (float): Stores how often to shoot a bullet
    """
    def __init__(self, cooldown_time):
        self.cooldownValue = cooldown_time
        self.cooldownTime = cooldown_time
        
class Size:
    """
    Holds size of non-sprite entities such as stars

    Attributes:
        size (int, int): Stores width and height of entity
    """
    def __init__(self, width, height):
        self.size = (width, height)
        
class Points:
    """
    Stores player's current point value

    Attributes:
        points (int): Current number of points player has earned
    """
    def __init__(self):
        self.points = 0

    """
    Updates player's point value whenever they kill an alien
    """ 
    def update(self):
        std_dev = (120 - 100) / 3
        num = round(random.gauss(100, std_dev))
        num = max(min(num, 120), 80)
        self.points += num