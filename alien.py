# Eugene Cook
# April 12, 2025
# Alien Invasion Game Alien

"""
    alien.py

    This module contains the functions to create an alien object

    Modules:
        - pygame
        - pygame.sprite
        - typing
        - alien_invasion
"""


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class representing a single alien

    Args:
        Sprite (_type_): _description_

    Attributes:
    game: instance of 'AlienInvasion'
    x: location on x-axis
    y: location on y-axis

    Mehtods:
    update(): update location of alien
    draw_bullet(): draw alien to the screen
    """
    def __init__(self, game: 'AlienInvasion', x: float, y: float) -> None:
        """Initialize alien with a game

        Args:
            game (AlienInvasion): Instance of a game
            x: x-axis
            y: y:axis
        """
        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,(self.settings.alien_w, self.settings.alien_h))
        # Rotated image
        self.image = pygame.transform.rotate(
            self.image, 270)
        
        # Moved image position to midleft to match new ship position
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        # self.rect.midleft = game.ship.rect.midleft
        # self.x = float(self.rect.x)

    def update(self) -> None:
        """Update location of alien
        """
        pass

    def draw_alien(self) -> None:
        """Draw alien to the screen
        """
        self.screen.blit(self.image, self.rect)