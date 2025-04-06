# Eugene Cook
# April 6, 2025
# Alien Invasion Game Arsenal's Ammo

"""
    bullet.py

    This module contains the functions to create a bullet object

    Methods:
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

class Bullet(Sprite):
    """A class representing ammo in an arsenal

    Args:
        Sprite (_type_): _description_

    Attributes:
    game: instance of 'AlienInvasion'

    Mehtods:
    update(): update location of fired ammo
    draw_bullet(): draw fired ammo to screen
    """
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize bullet with a game

        Args:
            game (AlienInvasion): Instance of a game
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,(self.settings.bullet_w, self.settings.bullet_h))
        # Rotated image
        self.image = pygame.transform.rotate(
            self.image, 270)
        
        # Moved image position to midleft to match new ship position
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midleft
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Update location of fired ammo
        """
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Draw fired ammo to screen
        """
        self.screen.blit(self.image, self.rect)