import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class AlienFleet:

    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()
    
    def create_fleet(self) -> None:
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h

        fleet_h = self.calculate_fleet_size(alien_h, screen_h)

        # half_screen = self.settings.screen_h
        fleet_vertical_space = fleet_h * alien_h
        y_offset = int((screen_h - fleet_vertical_space)//2)

        for row in range(fleet_h):
            current_y = alien_h * row + y_offset
            self._create_alien(current_y, 10)

    def calculate_fleet_size(self, alien_h, screen_h) -> any:
        fleet_h = (screen_h // alien_h)

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return fleet_h
    
    def _create_alien(self, current_y: int, current_x: int):
        new_alien = Alien(self, current_y, current_x)

        self.fleet.add(new_alien)

    def draw(self):
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()