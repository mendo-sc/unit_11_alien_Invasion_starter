""" 
game_stats
<<<<<<< HEAD

Defines the GameStats class for updating score, max score, hi-score, life count, and level.
"""
=======
Defines the GameStats class for updating game scores and level.
"""

>>>>>>> 33612cdc618c2043756f295e5819e186bf979f67
from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """ Class representing game statuses"""
    
    def __init__(self, game: 'AlienInvasion') -> None:
        """ Initializes the game stats and resets stats except saved hi-score

        Args:
            game (AlienInvasion): Instance of AlienInvasion
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()
    
    def init_saved_scores(self) -> None:
        """ Initializes the hi-score stat """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 0:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_score()

    def save_score(self) -> None:
        """ Saves hi-score """
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self) -> None:
        """ Resets ship count, session score, and level """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions: dict[any, list]) -> None:
        """ Updates score, max score, and hi-score

        Args:
            collisions (dict[any, list]): Bullet and alien collisions
        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self) -> None:
        """ Updates the max score of current session """
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self) -> None:
        """ Updates the hi-score """
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions: dict[any, list]) -> None:
        """ Updates the score based on alien destroyed

        Args:
            collisions (dict[any, list]): Bullet and alien collisions
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points
    
    def update_level(self) -> None:
        """ Increases level by 1 """
        self.level += 1
        