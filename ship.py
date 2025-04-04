import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """ A class representing the spaceship """

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (
            self.settings.ship_w, self.settings.ship_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.rect = self.image.get_rect()
        self.rect.midright = self.boundaries.midright
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal
    
    def update(self):
        """ Update ship position and arsenal """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """ Update ship movement within boundaries """
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y

    def draw(self) -> None:
        """ Draws arsenal and ship """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """ Fires bullet

        Returns:
            True: if bullet can be fired
            False: if bullet cannot be fired
        """
        return self.arsenal.fire_bullet()
