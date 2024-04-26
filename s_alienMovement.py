class AlienMovement:
    def moveAliens(self, dt, aliens_entities, alienBullet_entity, frame_count):
        """
        Move the aliens based on their movement patterns.

        Args:
            dt (float): The time step for the movement.
            aliens_entities (AliensEntities): The entity containing the aliens' movement data.
            alienBullet_entity (AlienBulletEntity): The entity for alien bullets.
            frame_count (int): The current frame count.

        Returns:
            None
        """
        for i, move in enumerate(aliens_entities.movement):
            if move.fn != None:
                (x, y, inc) = move.fn(move)
                move.position.x = x
                move.position.y = y
                move.t += inc * dt
            else:
                move.position.x += dt * move.px
                move.position.y += dt * move.py
            # If alien is able to shoot again
            if aliens_entities.cooldown[i].cooldownValue <= 0:
                alienBullet_entity.add_alienBullet((move.position.x, move.position.y, 0, 600))
                aliens_entities.cooldown[i].cooldownValue = aliens_entities.cooldown[i].cooldownTime
            aliens_entities.cooldown[i].cooldownValue -= dt

    def moveAlienBullets(self, dt, alienBullet_entity):
        """
        Move the alien bullets and remove those that are off-screen.

        Parameters:
        - dt (float): The time step for the movement.
        - alienBullet_entity (AlienBulletEntity): The entity containing the alien bullets.

        Returns:
        - None

        """
        # Bullet Movement & deletion
        for mov in alienBullet_entity.movement:
            mov.position.y += dt * mov.vy
            # Remove bullets that are off-screen
            if mov.position.y < -20:
                alienBullet_entity.movement.remove(mov)


            
