# Eugene Cook
# April 13, 2025
# Alien Invasion Game

"""
    alien_invasion.py

    This module contains the MAIN functions to run Alien Invasion game.

    Modules:
        - sys
        - pygame
        - settings
        - game_stats
        - ship
        - arsenal
        - alien_fleet
        - time
"""

import sys
import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from time import sleep
from button import Button


class AlienInvasion:
    """Class representing the MAIN functions to run Alien Invasion game

        Attributes:
        event: key presses and key releases

        Methods:
    """

    def __init__(self) -> None:
        """Initializes game
        """
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)
        
        self.screen = pygame.display.set_mode((
            self.settings.screen_w,self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.impact_sound = pygame.mixer.Sound(self.settings.impact_sound)
        self.impact_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()

        self.play_button = Button(self, 'Play')
        self.game_active = False

    def run_game(self) -> None:
        """Initializes game loop
        """
        # Game loop
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_collisions(self)-> None:
        # Check collisions for ship with aliens:
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()

        # check collisions for aliens and bottom of screen
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
        # check collisions for projectiles and aliens
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        if collisions:
            self.impact_sound.play()
            self.impact_sound.fadeout(250)

        if self.alien_fleet.check_destroyed_status():
            self._reset_level()

    def _check_game_status(self)-> None:
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self._reset_level()
            sleep(0.5)
        else:
            self.game_active = False

    def _reset_level(self)-> None:
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()

    def restart_game(self)-> None:
        pass
        # set up dynamic Settings
        # reset game GameStats
        # update HUD scores
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update then draw background and ship to screen
        """
        self.screen.blit(self.bg, (0,0))        
        self.ship.draw()
        self.alien_fleet.draw_fleet()

        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)

        pygame.display.flip()

    def _check_events(self):
        """Check for QUIT, KEYDOWN, and KEYUP events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()

    # Changed events to up and down instead of left and right            
    def _check_keyup_events(self, event) -> None:
        """Check for release of a key

        Args:
            event (_type_): Key release up or down
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event) -> None:
        """Check for key presses

        Args:
            event (_type_): Key presses UP, DOWN, SPACE, and Q (Quit)
        """
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()        
        





if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
