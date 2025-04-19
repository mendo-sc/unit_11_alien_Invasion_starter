""" 
bullet
<<<<<<< HEAD

Defines the bullet class for each bullet in arsenal. Handles 
=======
Defines the bullet class for each bullet in arsenal
>>>>>>> 33612cdc618c2043756f295e5819e186bf979f67
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """ A class representing each bullet sprite """

    def __init__(self, game: 'AlienInvasion'):
        """ Initializes bullet with horizontal rotation

        Args:
            game (AlienInvasion): Instance of AlienInvasion
        """
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (
            self.settings.bullet_w, self.settings.bullet_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midleft
        self.x = float(self.rect.x)

    def update(self) -> None:
        """ Updates bullet movement """
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """ Draws bullet on screen """
        self.screen.blit(self.image, self.rect)
