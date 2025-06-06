""""
alien
<<<<<<< HEAD

Defines the Alien class for each alien in the alien fleet, handles drawing the alien, and updating movement.
=======
Defines the Alien class for each alien in the alien fleet
>>>>>>> 33612cdc618c2043756f295e5819e186bf979f67
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """ A class representing each alien sprite """

    def __init__(self, fleet: 'AlienFleet', y: float, x: float) -> None:
        """ Initilizes an alien with an x and y location and horizontal rotation """
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (
            self.settings.alien_w, self.settings.alien_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self) -> None:
        """ Updates alien movement """
        temp_speed = self.settings.fleet_speed

        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x
        
        
    def check_edges(self) -> bool:
        """ Check if alien is hitting boundaries

        Returns:
            True: if alien is past top or bottom of screen
            False: if alien is within bounds
        """
        return (self.rect.bottom >= self.boundaries.bottom or 
                self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        """ Draws alien on screen """
        self.screen.blit(self.image, self.rect)
