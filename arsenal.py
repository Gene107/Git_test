# Eugene Cook
# April 6, 2025
# Alien Invasion Game Ship's Arsenal

"""
    arsenal.py
    
    This module contains the functions to create an arsenal fired from a ship

    Returns:
        object: Group of ammo fired from a ship

    Modules:
        - pygame
        - bullet
        - typing
        - alien_invasion
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """A class representing an arsenal

        Attributes:
        game: Instance of 'AlienInvasion'

        Methods:
        update_arsenal(): update ammo that can be fired
        draw(): draw fired ammo
        fire_bullet(): fires ammo from the arsenal
        _remove_bullets_offscreen(): Removes bullets not on the screen
    
    """
    
    def __init__(self, game: 'AlienInvasion'):
        """Initialize a arsenal with a game 

        Args:
            game (AlienInvasion): Instance of 'AlienInvasion'
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Update ammo available to fire
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Removes fired ammo no longer on the screen
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.settings.screen_w:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draw fired ammo 
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire ammo from arsenal

        Returns:
            bool: Can ammo be fired
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False