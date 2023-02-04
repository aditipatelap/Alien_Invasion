import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class to manage bullets fired from the ship. """
    def __init__(self, screen, ship, ai_setting):
        """ Create a new bullet at ship's current location."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) with some width and height
        self.bullet_rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)

        # and now set at ships's correct position
        self.bullet_rect.centerx = ship.ship_rect.centerx
        self.bullet_rect.top = ship.ship_rect.top

        # Store the bullet's position as a decimal value.
        self.y = float(self.bullet_rect.y)

        self.color = ai_setting.bullet_color
        self.speed = ai_setting.bullet_speed
    
    def update(self):
        """ Move bullet upward side of the screen. """
        self.y -= self.speed
        self.bullet_rect.y = self.y
        # self.bullet_rect.y -= self.speed
    
    def draw_bullet(self):
        """ Draw the bullet on the screen. """
        pygame.draw.rect(self.screen, self.color, self.bullet_rect)
