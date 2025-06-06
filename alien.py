# Eugene Cook
# April 13, 2025
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
    from alien_fleet import AlienFleet

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
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initialize alien with a game

        Args:
            game (AlienInvasion): Instance of a game
            x: x-axis
            y: y:axis
        """
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

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
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self) -> None:
        """Update location of alien
        """
        temp_speed = self.settings.fleet_speed

        self.y -= temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self)-> bool:
        return (self.rect.bottom == self.boundaries.bottom
                 or self.rect.top == self.boundaries.top)


    def draw_alien(self) -> None:
        """Draw alien to the screen
        """
        self.screen.blit(self.image, self.rect)