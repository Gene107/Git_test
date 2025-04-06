import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    def __init__(self, game: 'AlienInvasion') -> None:
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
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        self.screen.blit(self.image, self.rect)