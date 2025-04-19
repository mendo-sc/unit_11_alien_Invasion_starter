""" 
arsenal
<<<<<<< HEAD

Defines the arsenal class for all bullets. Includes managing the number of available bullets and deleting them when passing the left boundary.
=======
Defines the arsenal class for all bullets
>>>>>>> 33612cdc618c2043756f295e5819e186bf979f67
"""
import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """ A class representing an arsenal group of all bullets """

    def __init__(self, game: 'AlienInvasion') -> None:
        """ Initializes the arsenal """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """ Updates arsenal """
        self.arsenal.update()
        self._remove_bullets_offscreen()
        
    def _remove_bullets_offscreen(self) -> None:
        """ Deletes bullets after passing the left boundary """
        for bullet in self.arsenal.copy():
            if bullet.rect.right <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """ Draws bullets in arsenal """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """ Adds bullet to arsenal if within bullet_amount limit

        Returns:
            True: if arsenal has less bullets than limit
            False: if arsenal cannot hold another bullet
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False