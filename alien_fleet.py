""" 
alien_fleet

Defines the AlienFleet class. It creates the fleet and manages movement for bouncing off the boundaries.
"""
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class AlienFleet:
    """ A class representing the fleet of all aliens """

    def __init__(self, game: 'AlienInvasion') -> None:
        """ Initializes the fleet 

        Args:
            game (AlienInvasion): instance of AlienInvasion
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()
    
    def create_fleet(self) -> None:
        """ Creates the alien fleet """
        alien_h = self.settings.alien_h
        alien_w = self.settings.alien_w
        screen_h = self.settings.screen_h
        screen_w = self.settings.screen_w

        fleet_h, fleet_w = self.calculate_fleet_size(alien_h, screen_h, alien_w, screen_w)
        y_offset, x_offset = self.calculate_offsets(alien_h, alien_w, screen_h, fleet_h, fleet_w)

        self._create_rectangle_fleet(alien_h, alien_w, fleet_h, fleet_w, y_offset, x_offset)

    def _create_rectangle_fleet(self, alien_h: int, alien_w: int, fleet_h: int, fleet_w: int, y_offset: int, x_offset: int) -> None:
        """ Places the aliens by rows and columns 

        Args:
            alien_h (int): height of alien
            alien_w (int): width of alien
            fleet_h (int): height of fleet
            fleet_w (int): width of fleet
            y_offset (int): offset of y
            x_offset (int): offset of x
        """
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_y = alien_h * row + y_offset
                current_x = alien_w * col + x_offset
                if row % 2 == 0 or col % 2 == 0:
                    continue
                self._create_alien(current_y, current_x)

    def calculate_offsets(self, alien_h: int, alien_w: int, screen_h: int, fleet_h: int, fleet_w: int) -> tuple[int, int]:
        """Calculates the x and y offsets of the alien fleet

        Args:
            alien_h (int): height of alien
            alien_w (int): width of alien
            screen_h (int): height of screen
            fleet_h (int): height of fleet
            fleet_w (int): width of fleet

        Returns:
            tuple[int, int]: x and y offset value
        """
        half_screen = self.settings.screen_h
        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_w
        y_offset = int((screen_h - fleet_vertical_space)//2)
        x_offset = int((half_screen - fleet_horizontal_space)//2)
        return y_offset,x_offset

    def calculate_fleet_size(self, alien_h: int, screen_h: int, alien_w: int, screen_w: int) -> tuple[int, int]:
        """ Calculates the size of alien fleet

        Args:
            alien_h (int): height of alien
            screen_h (int): height of screen
            alien_w (int): width of alien
            screen_w (int): width of screen

        Returns:
            tuple[int, int]: height and width of fleet
        """
        fleet_h = (screen_h // alien_h)
        fleet_w = ((screen_w / 2) // alien_w)

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        return int(fleet_h), int(fleet_w)
    
    def _create_alien(self, current_y: int, current_x: int) -> None:
        """ Adds an alien to fleet 

        Args:
            current_y (int): current y value 
            current_x (int): current x value
        """
        new_alien = Alien(self, current_y, current_x)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self) -> None:
        """ Checks fleet direction if hitting boundary """
        alien: 'Alien'
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break
    
    def _drop_alien_fleet(self) -> None:
        """ Drops alien fleet towards ship """
        for alien in self.fleet:
            alien.x += self.fleet_drop_speed
            
    def update_fleet(self) -> None:
        """ Updates the fleet """
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self) -> None:
        """ Draws each alien """
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group: any) -> dict[any, list]:
        """Checks for bullet alien collisions

        Args:
            other_group (any): other group to check collision with

        Returns:
            dict[any, list]: dictionary of collided items
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_right(self) -> bool:
        """ Checkes if fleet hits right boundary

        Returns:
            True: if an alien hits right boundary
            False: if alien is not hitting right boundary
        """
        alien: 'Alien'
        for alien in self.fleet:
            if alien.rect.right >= self.settings.screen_w:
                return True
        return False
    

    def check_destroyed_status(self) -> bool:
        """ Checks if whole fleet destroyed

        Returns:
            True: if not alien in fleet
            False: if aliens in fleet
        """
        return not self.fleet