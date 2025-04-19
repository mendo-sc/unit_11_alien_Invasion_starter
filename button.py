""" 
button

Defines the button class for the play button.
"""
import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """ Class representing the play button """

    def __init__(self, game: 'AlienInvasion', msg: str) -> None:
        """ Initializes the play button

        Args:
            game (AlienInvasion): Instance of AlienInvasion
            msg (str): Text to show on button
        """
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(
            self.settings.font_file, self.settings.button_font_size
        )
        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)
        
    def _prep_msg(self, msg: str) -> None:
        """ Prepares message to place in the center of button

        Args:
            msg (str): Text to show on buttom
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """ Draws button with message """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos: tuple[int, int]) -> bool:
        """ Checks if mouse on button during click

        Args:
            mouse_pos (tuple[int, int]): the position of the mouse

        Returns:
            True: if button collides with mouse position
            False: if button not colliding with mouse
        """
        return self.rect.collidepoint(mouse_pos)
