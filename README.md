# Galaga
![galaga1](https://github.com/hkomal01/galaga/assets/98800239/9a7de6a3-6d05-4a77-8d35-1e54a2c99d72)
## Description:
A version of Galaga which was made to be concurrent. Currently, there is a 
single level implemented with multiple threads controlling each system of 
the game.
## Features:
- One level
- Enemy AI and movement implemented
- Can win or lose the level if you lose all of your health
- Point system
## Files
- game.py
    - This is the file which contains our main game loop and also spawns 
    the threads to control all of our different entities and systems. This
    is also the file which houses our main function and is used to start
    the game
- c_components.py
    - This file contains all the definitions for all of the components that
    are used to create the entities. 
- e_entity.py
    - This file contains all of the definitions for the different types of 
    entities that we have in our game. This includes defintions for the
    player ship entity, enemy alien entities, explosion entities, and 
    bullet entities.
- s_alienmovement.py
    - This file implements the system for alien movement. It is the system
    which updates all components of all aliens to reflect their current
    position on the screen and also controls when they shoot. 
- s_shipmovement.py
    - This file implements the system for the player ship movement. It reads
    in the player input from the InputState component and moves the ship
    accordingly. It also controls reading input for when players shoot.
- s_collisionDetection.py
    - This file implements the system for all collisions in our game. This
    includes bullets colliding with entities as well as the player ship 
    colliding with aliens. 
- s_explosion.py
    - This file implements the system for spawning, animating, and deleting
    all explosions on screens. 
- s_stars.py
    - This file implements the system which controls the stars spawning in the
    background of our game. It spawns them individually in random positions and
    then controls their motions.
- s_renderingSystem.py
    - This file implements the system for rendering everything on screen. It 
    will read data after it has been modified by all our systems each frame
    and will render the entities, entity bullets, and the background.
- sounds/
    - This folder contains the different sounds used for our game which 
    currently holds the background music as well as the bullet sounds.
- sprites/
    - This folder contains the sprites used for the ship, the aliens, and every
    frame of the explosion animation.
## Dependencies
To run the game you will need:
- Pygame
- Numpy
## How to play
Run:
```console
python3 game.py
```
