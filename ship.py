# Eugene Cook
# April 6, 2025
# Alien Invasion Game Ship

"""
    ship.py

    This module contains the functions to create a ship object

    Returns:
        Object: A ship object that can move vertically and fire ammo 
                horizontally

    Modules:
        - pygame
        - typing
        - alien_invasion
        - arsenal
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class representing a single ship

        Attributes:
        Game: Instance of AlienInvasion
        Arsenal: Group of ammo that can be fired

        Methods:
        update(): update ship movement and arsenal
        draw(): draw ship and fired ammo
        fire(): shoot ammo from arsenal

    """

    def __init__(self, game: 'AlienInvasion', arsenal: "Arsenal") -> None:
        """Initializes the ship object with a game and arsenal

        Args:
            game (AlienInvasion): _description_
            arsenal (Arsenal): Group of ammo to be fired from ship
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,(self.settings.ship_w, self.settings.ship_h))
        # Rotated image
        self.image = pygame.transform.rotate(
            self.image, 270)
        
        self.rect = self.image.get_rect()
        self._center_ship()
        # Changed ship movement direction
        self.moving_up = False
        self.moving_down = False
        self.arsenal = arsenal

    def _center_ship(self):
        # Changed ship rect location
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Update ship's movement and arsenal's ammo
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Update ships movement
        """
        # Changed movement from x axis to y axis
        temp_speed = self.settings.ship_speed
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed

        self.rect.y = self.y


    def draw(self) -> None:
        """Draw ship and fired ammo
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Fire ammo from arsenal

        Returns:
            bool: Was ammo fired
        """
        return self.arsenal.fire_bullet()