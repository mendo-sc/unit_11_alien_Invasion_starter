import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """ A class representing each alien sprite """
    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (
            self.settings.alien_w, self.settings.alien_h)
            )
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """ Updates alien movement """
        temp_speed = self.settings.fleet_speed
        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.x += self.settings.fleet_drop_speed

        self.y += temp_speed * self.settings. fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x
        
        
    def check_edges(self):
        return (self.rect.bottom >= self.boundaries.bottom or 
                self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        """ Draws alien on screen """
        self.screen.blit(self.image, self.rect)
